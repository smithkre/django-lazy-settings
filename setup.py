from distutils.core import setup
setup(
  name = 'django-lazy-settings',
  packages = ['lazy_setting', 'lazy_setting.templatetags'],
  version = '1.0',
  description = 'An easy way to use settings variable in django template.',
  author = 'Smith Krengkrud',
  author_email = 'smith.kre@gmail.com',
  url = 'https://github.com/smithkre/django-lazy-settings',
  download_url = 'https://github.com/smithkre/django-lazy-settings/archive/1.0.tar.gz',
  keywords = ['django', 'settings'],
  classifiers = [],
)