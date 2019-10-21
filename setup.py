from distutils.core import Extension
from distutils.core import setup

jitterentropy = Extension(
    "jitterentropy",
    include_dirs=["/usr/local/include"],
    libraries=["jitterentropy"],
    sources=["jitterentropy.c"],
)

setup(
    name="jitterentropy",
    version="0.1",
    description="Use libjitterentropy to get random bytes",
    author="Steve Wills",
    author_email="steve@mouf.net",
    url="https://github.com/swills/py-jitterentropy",
    long_description="""
Wrapper for libjitterentropy

See:

https://github.com/smuellerDD/jitterentropy-library
http://www.chronox.de/jent.html

""",
    ext_modules=[jitterentropy],
)
