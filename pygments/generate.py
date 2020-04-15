#!/usr/bin/env python

import os

from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter

PYGMENTS_PATH = './../static/pygments'


def export():
    if not os.path.exists(PYGMENTS_PATH):
        os.makedirs(PYGMENTS_PATH)

    styles = list(get_all_styles())

    for style in styles:
        print('Generating CSS for %s' % style)

        opts = {
            'style': style,
            'noclasses': False,
            'nobackground': False,
        }

        path = os.path.join(PYGMENTS_PATH, '%s.css' % style)
        formatter = HtmlFormatter(**opts)
        md_css = formatter.get_style_defs('.highlight')
        rst_css = formatter.get_style_defs('.literal-block')

        with open(path, 'w+') as f:
            f.write(md_css)
            f.write('\n')
            f.write(rst_css)


if __name__ == '__main__':
    export()
