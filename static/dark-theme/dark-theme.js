function ThemeManager(options) {
  var defaultTheme = options.defaultTheme;
  var enableAutoDetectTheme = options.enableAutoDetectTheme.toLowerCase() === 'true';

  var darkThemeMatch = window.matchMedia(
    defaultTheme === 'light' ?
      '(prefers-color-scheme: dark)' :
      '(prefers-color-scheme: dark), (prefers-color-scheme: no-preference)'
  );

  function setEnabledAndDisableMediaQuery(elementId, enabled) {
    var element = document.getElementById(elementId);
    element.disabled = !enabled;
    element.media = '';
  }

  function detectThemeAndSwitchStyle() {
    var theme = localStorage.getItem('themeOverride');
    if (theme !== 'light' && theme !== 'dark') {
      if (theme === 'browser' || enableAutoDetectTheme) {
        theme = darkThemeMatch.matches ? 'dark' : 'light';
      } else {
        theme = defaultTheme;
      }
    }

    // (Dis|En)able the styles according to the user's desired theme.  Get rid
    // of the media queries, since we are handling it in JS.
    setEnabledAndDisableMediaQuery('dark-theme-style', theme === 'dark');
    setEnabledAndDisableMediaQuery('pygments-dark-theme', theme === 'dark');
    setEnabledAndDisableMediaQuery('pygments-light-theme', theme === 'light');

    if (theme === 'dark') {
      document.body.classList.add('dark-theme');
      document.body.classList.remove('light-theme');
    } else {
      document.body.classList.add('light-theme');
      document.body.classList.remove('dark-theme');
    }
  }

  this.switch = function(themeOverride) {
    localStorage.setItem('themeOverride', themeOverride);
    detectThemeAndSwitchStyle();
  };

  // If there's an override, then apply it, otherwise, don't incur the
  // overhead of determining whether or not to switch themes.
  var themeOverride = localStorage.getItem('themeOverride');
  if (themeOverride === 'light' || themeOverride === 'dark') {
    detectThemeAndSwitchStyle();
  }

  // If theme auto-detection is enabled, then add a listenr on the matchMedia.
  darkThemeMatch.addListener(detectThemeAndSwitchStyle);
}

window.theme = new ThemeManager(document.getElementById('dark-theme-script').dataset);
