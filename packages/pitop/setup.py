"""pi-top Python SDK."""

import os
import sys
from setuptools import setup, find_packages

if not sys.version_info >= (3, 7):
    raise ValueError("This package requires Python 3.7 or above")

HERE = os.path.abspath(os.path.dirname(__file__))

__version__ = '0.0.1'
assert __version__ != ""

__project__ = "pitop"
__author__ = "pi-top"
__author_email__ = "deb-maintainers@pi-top.com"

__url__ = "https://github.com/pi-top/pi-top-Python-SDK"
__platforms__ = "ALL"

# https://pypi.org/classifiers/
__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "Topic :: Education",
    "Topic :: System :: Hardware",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy",
]

__keywords__ = [
    "pi-top",
    "raspberrypi",
    "gpio",
]

__requires__ = [
    ###############
    # Subpackages #
    ###############
    "pitop.system==0.0.1",
    "pitop.core==0.0.1",
    "pitop.pma==0.0.1",
    "pitop.camera==0.0.1",
    "pitop.keyboard==0.0.1",

    ####################################
    # Utilities - functions, IDs, etc. #
    ####################################
    "pitopcommon>=0.8.8,<0.9.0",

    #########
    # PROTO #
    #########
    # To use GPIO & components
    "gpiozero>=1.6.2,<1.7",

    #########
    # Pulse #
    #########
    "pyserial>=3.4,<3.5",

    #############
    # Webserver #
    #############
    "flask>=1.0.2,<1.1",
    "flask-cors>=3.0.7,<3.1",
    "flask-sockets>=0.2.1,<0.3",
    "gevent>=1.3.7,<1.4",
    "gevent-websocket>=0.10.1,<0.11.0",
]


def main():
    import io
    with io.open(os.path.join(HERE, "README.rst"), "r") as readme:
        setup(
            name=__project__,
            version=__version__,
            description=__doc__,
            long_description=readme.read(),
            classifiers=__classifiers__,
            author=__author__,
            author_email=__author_email__,
            url=__url__,
            license=[
                c.rsplit("::", 1)[1].strip()
                for c in __classifiers__
                if c.startswith("License ::")
            ][0],
            keywords=__keywords__,
            packages=find_packages(),
            include_package_data=True,
            platforms=__platforms__,
            install_requires=__requires__,
        )


if __name__ == "__main__":
    main()
