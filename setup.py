from setuptools import Extension
from setuptools import setup

jitterentropy = Extension(
    "jitterentropy",
    include_dirs=["/usr/local/include"],
    libraries=["jitterentropy"],
    sources=["jitterentropy.c"],
)

setup(
    name="jitterentropy",
    description="Use libjitterentropy to get random bytes",
    url="https://github.com/swills/py-jitterentropy",
    version="0.1",
    author="Steve Wills",
    author_email="steve@mouf.net",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    py_modules=["jitterentropy"],
    ext_modules=[jitterentropy],
    install_requires=[],
)
