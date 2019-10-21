from distutils.core import setup, Extension

jitterentropy = Extension('jitterentropy',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '1')],
                    include_dirs = ['/usr/local/include'],
                    libraries = ['jitterentropy'],
                    sources = ['jitterentropy.c'])

setup (name = 'jitterentropy',
       version = '0.1',
       description = 'This is a jitterentropy package',
       author = 'Steve Wills',
       author_email = 'steve@mouf.net',
       url = 'https://github.com/swills/py-jitterentropy',
       long_description = '''
Wrapper for libjitterentropy
''',
       ext_modules = [jitterentropy])
