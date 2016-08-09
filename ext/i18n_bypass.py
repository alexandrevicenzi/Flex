import jinja2.ext

class ByPassTrans(jinja2.ext.InternationalizationExtension):

    def __init__(self, environment):
      super(ByPassTrans, self).__init__(environment)
      self._install_null()


i18n = ByPassTrans
