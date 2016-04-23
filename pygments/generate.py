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
        }

        path = os.path.join(PYGMENTS_PATH, '%s.css' % style)
        formatter = HtmlFormatter(**opts)
        css_content = formatter.get_style_defs()
        # little fix because pelican doesn't append background color.
        css_content = css_content.replace('.hll', '.highlight')

        with open(path, 'w') as f:
            f.write(css_content)


if __name__ == '__main__':
    export()
