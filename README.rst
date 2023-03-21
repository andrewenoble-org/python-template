###############
Python Template
###############

|Contributor Covenant|

TO DO:
- Fix .github/workflows
- Fix badge, add more badges
- Create utils/yamler.py, utils/logger.py
- Copy this README to README.template.rst
- Add a new README describing how to automatically transform template into your own repo with python_template -> your repo name, name -> your name, email -> your email, etc.
- Add a note that README.rst should be removed and README.template.rst should be renamed README.rst (or let the script do this automatically)

========
Overview
========

A Python Template repo.

Read the `docs <https://github.com/>`_.

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

.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg :target: code_of_conduct.md
