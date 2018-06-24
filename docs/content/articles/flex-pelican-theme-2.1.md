Title: Flex 2.1.0
Date: 2016-11-16 08:00
Modified: 2016-11-16 08:00
Category: News
Tags: pelican, python, theme
Slug: flex-pelican-theme-update-2-1
Cover: images/flex-screenshot.png

[Flex theme](https://github.com/alexandrevicenzi/Flex) 2.1.0 comes with features that I was delaying for so long.

Flex 2.1.0 adds support for Google AdSense.

If you choose wisely, ads are a way to win some money, but if not, you may loose your users due to excessive use of ads.

Flex has six places for ads. Google recommends up to 3 ads per page. There is ads page only, and banner that appears on all pages.
Below you can see how to enable ads in your pelican configuration file.

```python
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-1234567890',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
```

Version 2.1.0 also comes with new translations. You can see available translations [here](https://github.com/alexandrevicenzi/Flex/wiki/Translations).

Hope you enjoy this version.
