#########
REPO_NAME
#########

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

========
Overview
========

GITHUB_REPO_DESCRIPTION

============
Installation
============

.. code:: bash

   $ python -m pip install 'python-template @ git+https://github.com/andrewenoble-org/python-template'

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

      $ pytest --cov --cov-report term-missing

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
