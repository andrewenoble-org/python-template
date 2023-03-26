# Contributing Guidelines

All types of contributions are welcome!

## Table of Contents

* [Code-of-Conduct](#code-of-conduct)
* [Asking a Question](#asking-a-question)
* [Contributing](#contributing)
* [Legal Notice](#legal-notice)

## Code-of-Conduct

This project and everyone participating in it is governed by a standard
[Code of Conduct](https://github.com/andrewenoble-org/python-template/main/.github/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable
behavior to
[andrew.e.noble@gmail.com](andrew.e.noble@gmail.com).

## Asking a Question

Please first check if current
[GitHub Pages](https://andrewenoble-org.github.io/python-template/)
or Issues linked to existing
[GitHub Projects](https://github.com/andrewenoble-org/python-template/projects)
address the question

If you still have a question or would appreciate further clarification, please open a
new
[GitHub Issue](https://github.com/andrewenoble-org/python-template/issues/new)
and carefully fill out the template with all requested information.

## Contributing

Please follow these steps to open a new Issue and start work in a development (dev)
environment:

1. Check if current
   [GitHub Pages](https://andrewenoble-org.github.io/python-template/)
   or Issues linked to existing
   [GitHub Projects](https://github.com/andrewenoble-org/python-template/projects)
   are relevant to your bug report, feature request, or suggested enhancement
2. Open a new [GitHub Issue](https://github.com/andrewenoble-org/python-template/issues/new),
   carefully fill out the template with all requested information, and
   link the Issue to an existing Project
3. On your local machine, install and launch
   [Docker Desktop](https://docs.docker.com/desktop/)
   and
   [VSCode](https://code.visualstudio.com/download)
4. Clone the repository

   ```bash
   git clone https://github.com/andrewenoble-org/python-template.git
   ```

5. Descend into the repository and checkout a dev branch

   ```bash
   cd python-template && git checkout -b <project-short-description>-<issue-number>-<issue-short-title>
   ```

6. Make dev image and container.  Also setup fake config for local `git` user to avoid
   `git` CLI errors

   ```bash
   make build && make run && make git-config
   ```

7. Open VSCode, install
   [Docker Extension](https://code.visualstudio.com/docs/containers/overview),
   and follow the Docker Extension instructions to attach a VSCode Window to your
   Docker container

8. Install [pre-commit](https://pre-commit.com/) within your dev container to activate
   hooks

   ```bash
   pre-commit install
   ```

9. To run tests and check coverage, use

   ```bash
   make test
   ```

10. Install additional VSCode Extensions to enable, within a single Window,
    syntax highlighting,
    rendered document previews,
    and Jupyter notebooks

      a. Better TOML
      b. HTML Preview
      c. Jupyter
      d. markdownlint
      e. reStructuredText
      f. reStructuredText Syntax highlighting
      g. Preview
      h. Python
      i. Pylance
      j. sqlfluff
      k. YAML

11. Make changes, following coding conventions listed below, expanding test coverage,
    and improving documentation
12. Check that all new and existing tests pass.  Carefully review changes for bugs
13. Commit changes, resolving any issues flagged by [pre-commit](https://pre-commit.com/)
14. Open a Pull Request, and carefully fill out the template with all requested
    information
15. Immediately before your final Squash and Merge to `main` within the GitHub UI,
    navigate to the top level of the respository, and run

   ```bash
   make test

   git add . && git commit -m "log final code coverage estimate" && git push
   ```

   to ensure that the code coverage estimate is correct.

Please follow these coding conventions:

1. Enforce [PEP8](https://peps.python.org/pep-0008/) with
  [pre-commit](https://pre-commit.com/).  See
  [pre-commit configs](https://github.com/andrewenoble-org/python-template/main/.github/CODE_OF_CONDUCT.md)
  for details
2. Use [numpydoc](https://numpydoc.readthedocs.io/en/latest/index.html) docstring style
3. Use meaningful, human-readable names for variables, classes, etc.
4. Avoid complex code blocks.  If required, carefully comment the code block

Note: These instructions have been tested on a MacBookPro with

* MacOSX Ventura v13.2.1,
* Docker v20.10.23, build 7155243, and
* VSCode v1.76.2 (Universal)
* python v3.8.2

Note: CODE_OF_CONDUCT.md requires :code:`[INSERT CONTACT METHOD]`

## GitHub Worflow

1. Open Issues within a Project
2. Checkout an Issue branch to do the work
3. Once PR is merged, delete the Issue branch from both local machine and GitHub

## Legal Notice

When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.
