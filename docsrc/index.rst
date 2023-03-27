###############
Python Template
###############

.. image:: https://img.shields.io/badge/doc-latest-blue.svg
   :target: https://andrewenoble-org.github.io/python-template/
   :alt: Docs

.. image:: https://img.shields.io/badge/python-3.9%7C3.10-blue.svg
   :target: https://img.shields.io/badge/python-3.9%7C3.10-blue.svg
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/l/tox?style=flat-square
   :target: https://opensource.org/licenses/MIT
   :alt: License

.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
   :alt: Code of Conduct

========
Overview
========

An opinionated Python Template GitHub repository enabling fast setup of boilerplate
code for :code:`pip`-installable packages with :code:`Docker`-ized
:code:`VSCode` Development Environments supporting

* :code:`Makefile` automating common Development Environment :code:`bash` commands
* :code:`pre-commit` hooks, including :code:`black` and :code:`isort`
* :code:`pytest` :code:`coverage` tracking
* Capturing all logging output in a single file, :code:`logs/logs.txt` by default
* :code:`jupyter` notebooks accessible either within a browser or within :code:`VSCode`
* Sphinx :code:`numpydoc` documentation deployed to :code:`GitHub Pages`
* README :code:`badges/shields`
* GitHub :code:`main` branch protection rules
* GitHub Issue and Pull-request templates
* Opening GitHub Issues within :code:`GitHub Projects` and automatically
  closing them with a Pull Request
* :code:`GitHub Actions` for testing and super-linting Pull Requests as well as tagging
  releases and updating :code:`GitHub Pages` with each merge to :code:`main`

See :code:`.github/CONTRIBUTING.md` for details on the recommended Development
Environment and GitHub configuration/workflow

.. note::
   This repository (the template) is not intended to be :code:`pip`-installable

=====
Usage
=====

#. Install and launch
   `Docker Desktop <https://docs.docker.com/desktop/>`_ and
   `VSCode <https://code.visualstudio.com/download>`_

#. Check that :code:`git` and :code:`python` are installed on your local machine,
   with :code:`python --version` `3.9` or `3.10`.  You may also need to
   :code:`pip install pyyaml`

#. Within your working directory, clone the repository to a directory with the same
   name as your repository and configure

   .. code:: bash

      $ GITHUB_REPO_NAME=<your-respository-name>
      $ mkdir $GITHUB_REPO_NAME
      $ git clone https://github.com/andrewenoble-org/python-template.git $GITHUB_REPO_NAME
      $ cd $GITHUB_REPO_NAME
      $ export PYTHONPATH=".:`pwd`"

#. Edit :code:`assets/template/template_custom.yml`, replacing the 7 placeholder values with
   the correct information for your repository

#. Run the template script to create your respository.  Note that this script will
   self-destruct (the final line deletes the :code:`assets/template` directory)

   .. code:: bash

      $ python assets/template/template.py

#. Your repository is ready for development! See :code:`.github/CONTRIBUTING.md` for
   the recommended Development Environment

.. note::
   These instructions have been tested on a MacBookPro with

   * MacOSX Ventura v13.2.1
   * Docker v20.10.23, build 7155243
   * VSCode v1.76.2 (Universal)
   * python v3.9.16
   * git v2.40.0

=================
Table of Contents
=================

.. toctree::
   :maxdepth: 1

   api
