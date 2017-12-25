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
        logo='logo ' + pycon,
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
        env = self.state.document.settings.env
        content = []
        codeblock = env.code_outs[self.arguments[0]]
        code_out_text = execute_codeblock(codeblock)
        if codeblock["language"] == "logo":
            element = nodes.image(uri=codeblock["screenshot_path"])
        else:
            element = nodes.literal_block(code_out_text, code_out_text)
            element['language'] = "console"
            element['linenos'] = False
        content.append(element)

        return content


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
            screenshot_path = os.path.join(statics_dir_path, "screenshot_%s.png" % key)
            env.code_outs[name] = dict(code=code, language=language, screenshot_path=screenshot_path)

        return [image]


def execute_codeblock(codeblock):
    code = codeblock["code"]
    config = AutoRun.config
    args = config['pycon'].split()
    # Build the code text
    env = os.environ.copy()
    env["SCREENSHOT_PATH"] = codeblock["screenshot_path"]
    proc = Popen(args, bufsize=1, stdin=PIPE, stdout=PIPE, stderr=PIPE, env=env)

    # Run the code
    stdout, stderr = proc.communicate(code)

    # Process output
    out = " "
    if stdout:
        out = stdout.decode("utf-8")
    if stderr:
        out = stderr.decode("utf-8")

    # Get the original code with prefixes
    code_out_text = out

    if code_out_text[0] == '\n':
        code_out_text = code_out_text[1:]

    proc.wait()

    return code_out_text


def setup(app):
    app.add_directive('code_example', RunBlock)
    app.add_directive('code_output', CodeOutput)
    app.connect('builder-inited', AutoRun.builder_init)
    app.add_config_value('code_example_languages', AutoRun.config, 'env')
