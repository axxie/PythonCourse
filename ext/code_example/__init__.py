# -*- coding: utf-8 -*-
"""
sphinxcontirb.autorun
~~~~~~~~~~~~~~~~~~~~~~

Run the code and insert stdout after the code block.
"""
import hashlib
import os
from subprocess import PIPE, Popen

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


class RunBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'linenos': directives.flag,
    }

    def run(self):
        # TODO: create images in TEMP and delete afterwards
        statics_dir_path = os.path.join(self.state.document.settings.env.app.builder.outdir, STATICS_DIR_NAME)
        config = AutoRun.config
        language = self.arguments[0]

        if language not in config:
            raise RunBlockError('Unknown language %s' % language)

        # Get configuration values for the language
        args = config[language].split()
        input_encoding = config.get(language + '_input_encoding', 'ascii')
        output_encoding = config.get(language + '_output_encoding', 'ascii')
        prefix_chars = config.get(language + '_prefix_chars', 0)
        show_source = config.get(language + '_show_source', True)

        codelines = (line[prefix_chars:] for line in self.content)
        code = u'\n'.join(codelines).encode(input_encoding)

        h = hashlib.sha1()
        h.update(code)
        key = h.hexdigest()

        file = os.path.join(statics_dir_path, "code_example_%s.png" % (key))
        args += [file]

        # Build the code text
        proc = Popen(args, bufsize=1, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        # Run the code
        stdout, stderr = proc.communicate(code)

        # Process output
        if stdout:
            out = stdout.decode(output_encoding)
        if stderr:
            out = stderr.decode(output_encoding)

        # Get the original code with prefixes
        if show_source:
            code = u'\n'.join(self.content)
        else:
            code = ''
        code_out = u'\n'.join((code, out))

        if code_out[0] == '\n':
            code_out = code_out[1:]

        image = nodes.image(uri=file)

        # TODO: add execution result where requested, not immediately after picture
        literal = nodes.literal_block(code_out, code_out)
        literal['language'] = language
        literal['linenos'] = 'linenos' in self.options
        return [image, literal]


def setup(app):
    app.add_directive('code_example', RunBlock)
    app.connect('builder-inited', AutoRun.builder_init)
    app.add_config_value('code_example_languages', AutoRun.config, 'env')
