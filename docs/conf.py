# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import importlib.util
import os
import sys

# -- Path setup --------------------------------------------------------------


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
HERE = os.path.abspath(os.path.dirname(__file__))
PARENT = os.path.dirname(HERE)
sys.path.append(f"{PARENT}/packages")

# -- Project information -----------------------------------------------------

# Get package version directly from file
#
# Importing 'pitop' requires all core dependencies to be installed
# which is impractical for building docs
spec = importlib.util.spec_from_file_location(
    "version", f"{PARENT}/packages/pitop/pitop/version.py"
)
modulevar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulevar)

project = "pitop"
author = "pi-top (CEED Ltd)"
release = os.environ.get("PYTHON_PACKAGE_VERSION", "0.0.1.dev1")
copyright = "pi-top 2022"

# -- General configuration ---------------------------------------------------

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

autosectionlabel_prefix_document = True

# Extension options
# TODO v2 of sphinx-common: `None` -> `True`
# see https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
autodoc_default_options = {
    "members": None,
    "member-order": "bysource",
    "undoc-members": None,
}

autodoc_warningiserror = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", ".api_advanced_usage.rst"]


# -- Intersphinx configuration --------------------------------------------

intersphinx_mapping = {
    "gpiozero": ("https://gpiozero.readthedocs.io/en/latest", None),
    "imageio": ("https://imageio.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "luma-oled": ("https://luma-oled.readthedocs.io/en/latest/", None),
    "Pillow": ("https://pillow.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3.7", None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_sidebars = {}

html_theme_options = {
    "canonical_url": "https://docs.pi-top.com/python-sdk/en/latest/?badge=latest",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#20b6aa",
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": False,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom stuff for project
autodoc_mock_imports = [
    "cv2",
    "flask",
    "flask_sockets",
    "numpy",
    "imageio",
    "imutils",
    "matplotlib",
    "Mock",
    "mpl_toolkits",
    "PIL",
    "pygame",
    "pyinotify",
    "RPi",
    "scipy",
    "serial",
    "smbus",
    "smbus2",
    "spidev",
    "zmq",
    "wget",
]

# -- Options for manual page output ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-man_pages
man_page_startdocname = "cli_tools"
man_page_name = "pi-top"
man_page_description = "pi-top Command Line Tool"
man_page_authors = [author]
man_page_section = 1
man_pages = [
    (
        man_page_startdocname,
        man_page_name,
        man_page_description,
        man_page_authors,
        man_page_section,
    )
]

man_show_urls = True
