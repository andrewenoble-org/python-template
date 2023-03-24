###############
Python Template
###############

.. image:: https://img.shields.io/badge/doc-latest-blue.svg
   :target: https://andrewenoble-org.github.io/python-template/
   :alt: Docs
   :align: center
.. image:: https://img.shields.io/pypi/l/tox?style=flat-square
   :target: https://opensource.org/licenses/MIT
   :alt: License
   :align: center
.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
   :alt: Code of Conduct
   :align: center
.. image:: assets/coverage/coverage.svg
   :target: https://github.com/andrewenoble-org/python-template/tree/main/assets
   :alt: Code Coverage
   :align: center

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
- Copy this README to README.template.rst
- Add a new README describing how to automatically transform template into your own repo with python_template -> your repo name, name -> your name, email -> your email, etc.
- Add a note that README.rst should be removed and README.template.rst should be renamed README.rst (or let the script do this automatically)

========
Overview
========

A Python Template repo.

============
Installation
============

\<Add pip installation instructions\>

============
Contributing
============

Setup a Development Environment using Docker, Make, and
`pre-commit <https://pre-commit.com/>`_.

#. Clone repo

#. Descend into repo

#. Make commands to create dev image and container

#. Install :code:`pre-commit` within your dev container to
   activate hooks

   .. code-block:: bash

      $ pre-commit install

#. Check pytest coverage with

   .. code-block:: bash

      $ pytest --cov --cov-report term-missing

#. Run in container, to obtain a sufficient, dummy git config

   .. code-block:: bash

      $ make git-config
