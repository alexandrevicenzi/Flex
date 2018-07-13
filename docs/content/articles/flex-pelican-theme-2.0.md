Title: Flex 2.0
Date: 2016-09-13 08:00
Modified: 2016-09-13 08:00
Category: News
Tags: pelican, python, theme
Slug: flex-pelican-theme-update-2-0
Cover: images/flex-screenshot.png

[Flex theme](https://github.com/alexandrevicenzi/Flex) 2.0 comes with new features.
In fact there are two new features.

The biggest change is localization support.
Yes, Flex now can be translated into your language.
You can read about [here](https://github.com/alexandrevicenzi/Flex/wiki/Translations).

The biggest challege was to create a way to translate without breaking old versions.
If you use English it changes nothing for you.
But if you want to use translation you need to add new lines to your pelican configuration file.

Here is a small example to use Flex in another language.

```python
# Enable i18n plugin, probably you already have some others here.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# Default theme language.
I18N_TEMPLATES_LANG = 'en'
# Your language.
DEFAULT_LANG = 'de'
OG_LOCALE = 'de_DE'
LOCALE = 'de_DE'
```

Last but not least, Flex supports the feature "X minute read", similar [Medium](https://medium.com/).

Hope you enjoy this version.
