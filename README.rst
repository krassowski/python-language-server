Python Language Server
======================

.. image:: https://github.com/krassowski/python-language-server/workflows/Linux%20tests/badge.svg
    :target: https://github.com/krassowski/python-language-server/actions?query=workflow%3A%22Linux+tests%22

.. image:: https://github.com/krassowski/python-language-server/workflows/Mac%20tests/badge.svg
    :target: https://github.com/krassowski/python-language-server/actions?query=workflow%3A%22Mac+tests%22

.. image:: https://github.com/krassowski/python-language-server/workflows/Windows%20tests/badge.svg
    :target: https://github.com/krassowski/python-language-server/actions?query=workflow%3A%22Windows+tests%22

.. image:: https://img.shields.io/github/license/krassowski/python-language-server.svg
     :target: https://github.com/krassowski/python-language-server/blob/master/LICENSE

A Python 3.6+ implementation of the `Language Server Protocol`_. A friendly fork of the `palantir/python-language-server`.

Major changes compared to upstream:

* added `completionItem/resolve` support to improve performance of completions
* implemented caching of completion labels for numpy, pandas, tensorflow and matplotlib for Jedi completions
* implemented a rule to not calculate labels for lists of completions exceeding specific number (25 by default)
* implemented conversion of ReStructuredText and Sphinx docstrings to Markdown (for Jedi hover and completions)
* multiple signatures no longer clobber the docstrings but instead are collapsed under "more signatures"
* improved sorting of completions (implemented token counter and better rules for `sortText`)
* dropped Python 2.7 support

Installation
------------

The base language server requires Jedi_ to provide Completions, Definitions, Hover, References, Signature Help, and
Symbols:

``pip install git+https://github.com/krassowski/python-language-server.git@main``

If the respective dependencies are found, the following optional providers will be enabled:

* Rope_ for Completions and renaming
* Pyflakes_ linter to detect various errors
* McCabe_ linter for complexity checking
* pycodestyle_ linter for style checking
* pydocstyle_ linter for docstring style checking (disabled by default)
* autopep8_ for code formatting
* YAPF_ for code formatting (preferred over autopep8)

Optional providers can be installed using the `extras` syntax. To install YAPF_ formatting for example:

``pip install 'python-language-server[yapf]'``

All optional providers can be installed using:

``pip install 'python-language-server[all]'``

If you get an error similar to ``'install_requires' must be a string or list of strings`` then please upgrade setuptools before trying again. 

``pip install -U setuptools``

3rd Party Plugins
~~~~~~~~~~~~~~~~~
Installing these plugins will add extra functionality to the language server:

* pyls-mypy_ Mypy type checking for Python 3
* pyls-isort_ Isort import sort code formatting
* pyls-black_ for code formatting using Black_

Please see the above repositories for examples on how to write plugins for the Python Language Server. Please file an
issue if you require assistance writing a plugin.

Configuration
-------------

Configuration is loaded from zero or more configuration sources. Currently implemented are:

* pycodestyle: discovered in ~/.config/pycodestyle, setup.cfg, tox.ini and pycodestyle.cfg.
* flake8: discovered in ~/.config/flake8, setup.cfg, tox.ini and flake8.cfg

The default configuration source is pycodestyle. Change the `pyls.configurationSources` setting to `['flake8']` in
order to respect flake8 configuration instead.

Overall configuration is computed first from user configuration (in home directory), overridden by configuration
passed in by the language client, and then overriden by configuration discovered in the workspace.

To enable pydocstyle for linting docstrings add the following setting in your LSP configuration:
```
"pyls.plugins.pydocstyle.enabled": true
```

See `package.json`_ for the full set of supported configuration options.

.. _package.json: vscode-client/package.json

Language Server Features
------------------------

Auto Completion:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/auto-complete.gif

Code Linting with pycodestyle and pyflakes:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/linting.gif

Signature Help:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/signature-help.gif

Go to definition:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/goto-definition.gif

Hover:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/hover.gif

Find References:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/references.gif

Document Symbols:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/document-symbols.gif

Document Formatting:

.. image:: https://raw.githubusercontent.com/palantir/python-language-server/develop/resources/document-format.gif

Development
-----------

Please branch of the `develop` branch which is being kept in sync with upstream rather than from the `main` branch
if possible, to allow to send pull requests upstream.

To run the test suite:

``pip install .[test] && pytest``


License
-------

This project is made available under the MIT License.

.. _Language Server Protocol: https://github.com/Microsoft/language-server-protocol
.. _Jedi: https://github.com/davidhalter/jedi
.. _Rope: https://github.com/python-rope/rope
.. _Pyflakes: https://github.com/PyCQA/pyflakes
.. _McCabe: https://github.com/PyCQA/mccabe
.. _pycodestyle: https://github.com/PyCQA/pycodestyle
.. _pydocstyle: https://github.com/PyCQA/pydocstyle
.. _YAPF: https://github.com/google/yapf
.. _autopep8: https://github.com/hhatto/autopep8
.. _pyls-mypy: https://github.com/tomv564/pyls-mypy
.. _pyls-isort: https://github.com/paradoxxxzero/pyls-isort
.. _pyls-black: https://github.com/rupert/pyls-black
.. _Black: https://github.com/ambv/black
