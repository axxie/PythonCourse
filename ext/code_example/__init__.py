# -*- coding: utf-8 -*-
"""
sphinxcontirb.autorun
~~~~~~~~~~~~~~~~~~~~~~

Run the code and insert stdout after the code block.
"""
import hashlib
import os
import os.path
import tempfile
from subprocess import PIPE, Popen, DEVNULL

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.errors import SphinxError
from sphinx_autorun import version

__version__ = version.version

STATICS_DIR_NAME = '_static'


class RunBlockError(SphinxError):
    category = 'runblock error'


class AutoRun(object):
    here = os.path.abspath(__file__)
    pycon = os.path.join(os.path.dirname(here), 'pycon.py')
    config = dict(
        pycon='python ' + pycon,
        pycon_prefix_chars=0,
        pycon_show_source=False,
        console='bash',
        console_prefix_chars=1,
    )

    @classmethod
    def builder_init(cls, app):
        cls.config.update(app.builder.config.code_example_languages)


class codeout_node(nodes.General, nodes.Element):
    pass


class CodeOutput(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        code_out = codeout_node()
        code_out['ref'] = self.arguments[0]
        return [code_out]


def render_source(source, image_path):
    new_file, filename = tempfile.mkstemp(suffix=".py")
    os.write(new_file, source)
    os.close(new_file)

    process = Popen(["cmd.exe", "/c", os.path.join(os.path.dirname(__file__), "convert.cmd"), filename, image_path],
                    stdout=DEVNULL, stderr=DEVNULL)
    process.wait()
    os.remove(filename)


class RunBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'linenos': directives.flag,
        'name': directives.unchanged
    }

    def run(self):
        # TODO: create images in TEMP and delete afterwards
        statics_dir_path = os.path.join(self.state.document.settings.env.app.builder.outdir, STATICS_DIR_NAME)
        config = AutoRun.config
        language = self.arguments[0]

        if language not in config:
            raise RunBlockError('Unknown language %s' % language)

        # Get configuration values for the language
        input_encoding = config.get(language + '_input_encoding', 'ascii')

        codelines = self.content[:]
        code = u'\n'.join(codelines).encode(input_encoding)

        h = hashlib.sha1()
        h.update(code)
        key = h.hexdigest()

        image_path = os.path.join(statics_dir_path, "code_example_%s.png" % key)
        render_source(code, image_path)

        image = nodes.image(uri=image_path)

        env = self.state.document.settings.env
        if not hasattr(env, 'code_outs'):
            env.code_outs = {}

        name = self.options.get('name')
        if name:
            env.code_outs[name] = code

        return [image]


def execute_codeblock(code):
    config = AutoRun.config
    args = config['pycon'].split()
    # Build the code text
    proc = Popen(args, bufsize=1, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Run the code
    stdout, stderr = proc.communicate(code)

    # Process output
    if stdout:
        out = stdout.decode("utf-8")
    if stderr:
        out = stderr.decode("utf-8")

    # Get the original code with prefixes
    code_out_text = out

    if code_out_text[0] == '\n':
        code_out_text = code_out_text[1:]

    return code_out_text


def process_codeblock_nodes(app, doctree, fromdocname):
    env = app.builder.env

    for node in doctree.traverse(codeout_node):
        content = []
        code_out_text = execute_codeblock(env.code_outs[node['ref']])
        literal = nodes.literal_block(code_out_text, code_out_text)
        literal['language'] = "console"
        literal['linenos'] = False
        content.append(literal)
        node.replace_self(content)


def setup(app):
    app.add_directive('code_example', RunBlock)
    app.add_directive('code_output', CodeOutput)
    app.connect('builder-inited', AutoRun.builder_init)
    app.connect('doctree-resolved', process_codeblock_nodes)
    app.add_config_value('code_example_languages', AutoRun.config, 'env')
