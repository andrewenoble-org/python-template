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

.. image:: assets/coverage/coverage.svg
   :target: https://github.com/andrewenoble-org/python-template/blob/main/assets/coverage/coverage.svg
   :alt: Code Coverage

|

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/merge_pages.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/merge_pages.yml/badge.svg
   :alt: Merge Pages

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/merge_release.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/merge_release.yml/badge.svg
   :alt: Merge Release

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/pr_lint.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/pr_lint.yml/badge.svg
   :alt: PR List

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/pr_test.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/pr_test.yml/badge.svg
   :alt: PR Test

========
Overview
========

A Python Template GitHub repository.

.. note::
   This template repository is not intended to be :code:`pip` installable.

=====
Usage
=====

#. Install and launch
   `Docker Desktop <https://docs.docker.com/desktop/>`_ and
   `VSCode <https://code.visualstudio.com/download>`_.

#. Check that :code:`git` and :code:`python` are installed on your local machine,
   with :code:`python --version >= 3.8.2`

#. Clone the repository to a folder with the same name as your repository

   .. code:: bash

      $ GITHUB_REPO_NAME=<your-respository-name>
      $ mkdir $GITHUB_REPO_NAME
      $ git clone https://github.com/andrewenoble-org/python-template.git $GITHUB_REPO_NAME
      $ cd $GITHUB_REPO_NAME
      $ git init

#. Edit :code:`assets/template/template.yml`, inserting your information

#. Run script to create your respository from the template

#. Make your initial commit and push to GitHub

#. Recommended GitHub repository configurations

.. note::
   These instructions have been tested on a MacBookPro with
   * MacOSX Ventura v13.2.1,
   * Docker v20.10.23, build 7155243, and
   * VSCode v1.76.2 (Universal)
   * python v3.8.2
   * git v2.30.2
