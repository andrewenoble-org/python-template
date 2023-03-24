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
   :target: https://github.com/andrewenoble-org/python-template/tree/main/assets
   :alt: Code Coverage

|

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/test.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/test.yml
   :alt: Tests

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/pages.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/pages.yml
   :alt: Docs

.. image:: https://github.com/andrewenoble-org/python-template/actions/workflows/lint.yml/badge.svg
   :target: https://github.com/andrewenoble-org/python-template/actions/workflows/lint.yml
   :alt: Lint

TO DO:
- Edit .github/workflow/pages.yaml to automatically deploy pages upon push to main
- Create .github/workflow/release.yaml to update version and tag releases upon push to main
- Possibly combine all pull_request and push jobs to two total workflow files
- Add a new README describing how to automatically transform template into your own repo with python_template -> your repo name, name -> your name, email -> your email, etc.
- Add a note that README.rst should be removed and README.template.rst should be renamed README.rst (or let the script do this automatically)

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

#. Clone the repository to a folder with the same name as your repository

   .. code:: bash

      $ GITHUB_REPO_NAME=<your-respository-name>
      $ git clone https://github.com/andrewenoble-org/python-template.git $GITHUB_REPO_NAME

#. Edit :code:`assets/template/template.yml`, inserting your information

#. Run script to create your respository from the template

#. Make your initial commit and push to GitHub

#. Recommended GitHub repository configurations

============
Contributing
============

Setup a Development Environment on your local machine using Docker Desktop, Make, and
`pre-commit <https://pre-commit.com/>`_.

#. Install and launch
   `Docker Desktop <https://docs.docker.com/desktop/>`_ and
   `VSCode <https://code.visualstudio.com/download>`_.

#. Clone the repository

   .. code:: bash

      $ git clone https://github.com/andrewenoble-org/python-template.git

#. Descend into the repository and checkout a dev branch

   .. code:: bash

      $ GIT_USERNAME=<git-username>
      $ cd python-template && git checkout $GIT_USERNAME-dev

#. Make dev image and container, adding a dummy git config

   .. code:: bash

      $ make build && make run && make git-config

#. Install :code:`pre-commit` within your dev container to activate hooks

   .. code-block:: bash

      $ pre-commit install

#. Check that tests pass and that coverage is consistent with the badge above

   .. code-block:: bash

      $ make test

#. Recommended VSCode Extensions

   #. Better TOML
   #. Docker
   #. HTML Preview
   #. Jupyter
   #. markdownlint
   #. reStructuredText
   #. reStructuredText Syntax highlighting
   #. Preview
   #. Python
   #. Pylance
   #. sqlfluff
   #. YAML

.. note::
   This setup has only been tested on
   MacOSX Ventura 13.2.1,
   Docker version 20.10.23, build 7155243, and
   VSCode 1.76.2 (Universal)
