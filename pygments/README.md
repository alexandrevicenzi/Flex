# Pygments CSS generator

This is the correct way to generate all pygments CSS files.

## How to generate CSSs files

Before run `generate.py` remember to install all requirements.
This can done with `pip install -r requirements.txt`.

After this you can run `./generate.py`. Remember to run inside this folder.
Because it uses relative path to place inside `static/pygments` folder.

After that, go back to the Flex path and run `gulp pygments` to generate all `min.css` files.

## How to add new styles?

[See wiki](https://github.com/alexandrevicenzi/Flex/wiki/Code-Highlight#how-to-add-new-styles).
