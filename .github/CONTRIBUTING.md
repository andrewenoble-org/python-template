# Contributing Guidelines

All types of contributions are welcome!

## Table of Contents

* [Code-of-Conduct](#code-of-conduct)
* [Asking a Question](#asking-a-question)
* [Contributing](#contributing)
* [Coding Conventions](#coding-conventions)
* [Development Environment](#local-development-environment)
* [GitHub Configuration](#github-configuration)
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

Please follow these steps to open a new GitHub Issue
(see [GitHub Configuration](#github-configuration) below)
ticketed to a GitHub Project,
make changes on a corresponding Issue branch within your local
`VSCode` Development Environment
(see [Development Environment](#local-development-environment) setup below)

1. Check if current
   [GitHub Pages](https://andrewenoble-org.github.io/python-template/)
   or Issues linked to existing
   [GitHub Projects](https://github.com/andrewenoble-org/python-template/projects)
   are relevant to your bug report, feature request, or suggested enhancement
2. Open a new
   [GitHub Issue](https://github.com/andrewenoble-org/python-template/issues/new),
   carefully fill-out the template with all requested information
3. Once the Issue is open, select a relevant
   [GitHub Project](https://github.com/andrewenoble-org/python-template/projects),
   select "Add item" on a view within that project, search for your Issue by typing
   :code:`#python-template` in the text box, and then add the Issue.
4. Within your local `VSCode` Development Environment (see setup below), start
   work on a development branch named for your specific Project and Issue

   ```bash
   \$ cd python-template
   \$ git checkout -b <project-short-description>-<issue-number>-<issue-short-title>
   \$ git push -u origin <project-short-description>-<issue-number>-<issue-short-title>
   ```

5. As you make changes, follow the [Coding Conventions](#coding-conventions) listed
   below, write tests to cover your changes, improve documentation to cover your
   changes, and make frequent commits with short commit messages following the
   [Anglar convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#type)

   ```bash
   \<type\>\(\<scope\>\): \<short summary\>
   ```

   where \<type\> is `build|ci|docs|feat|fix|perf|refactor|test`

6. Once your changes are made, all `pytest` tests pass locally, and
   `pre-commit run --all` runs without error, open a new
   [GitHub Pull Request](https://github.com/andrewenoble-org/python-template/compare)
   and trigger Pull Request
   [GitHub Actions](https://github.com/andrewenoble-org/python-template/actions)
   with a push from your local `VSCode` Development Environment

   ```bash
   make test && make git-push-f
   ```

   Iterate until all Pull-Request-triggered Actions run without error, including
      * `pr-lint`: runs the [super-linter](https://github.com/github/super-linter)
      * `pr-pages-qc`: checks that `./docsrc/build` runs without error
      * `pr-release`: increments the semantic version from the previous release
      * `pr-test`: runs `pytest` for python versions `3.9` and `3.10` and for operating
        systems `ubuntu-latest` and `macosx-latest`

7. Once all Pull-Request-triggered Actions run without error, carefully review the
   GitHub Pull-Request checklist and complete any missing action-items, including
   triple checks for any bugs
8. Once all action-items are complete, request a review on GitHub.  At least one
   review by one project owner is required
9. Once all conversation threads raised during review have been resolved, press
   `Squash and Merge` on GitHub to merge to `main`
10. Once Pull Request is merged, delete the Issue branch from both your `VSCode`
    Development Environment and GitHub

## Coding Conventions

1. Enforce [PEP8](https://peps.python.org/pep-0008/) with
  [pre-commit](https://pre-commit.com/).  See
  [pre-commit config file](https://github.com/andrewenoble-org/python-template/blob/main/.pre-commit-config.yaml)
  for details
2. Use [numpydoc](https://numpydoc.readthedocs.io/en/latest/index.html) docstring style
3. Use meaningful, human-readable names for variables, classes, etc.
4. Avoid complex code blocks.  If required, carefully comment the code block

## Local Development Environment

1. On your local machine, install and launch
   [Docker Desktop](https://docs.docker.com/desktop/)
   and
   [VSCode](https://code.visualstudio.com/download)
2. Clone the repository

   ```bash
   \$ git clone https://github.com/andrewenoble-org/python-template.git
   ```

3. Within the respository, build a Development Environment `Docker` image, deploy a
   Development Environment `Docker` container

   ```bash
   \$ make build && make run
   ```

4. Open `VSCode`, install
   [Docker Extension](https://code.visualstudio.com/docs/containers/overview),
   and follow the `Docker Extension` instructions to Attach a `VSCode` Window to your
   Docker container

5. Navigate at the top of the `VSCode` window to the `/home/project`.  This is the
   containerized Development Environment working directory
6. Setup a fake configuration for `git`, to avoid `git` CLI errors, by running in the
   `VSCode` terminal

   ```bash
   \$ make git-config
   ```

7. Install [pre-commit](https://pre-commit.com/) in your Development Environment
   container to activate hooks

   ```bash
   \$ pre-commit install
   ```

8. Check that your local Development Environment passes all `pre-commit` checks with

   ```bash
   \$ pre-commit run --all
   ```

9. Check that all tests pass with good coverage in your local Development Environment
   with

   ```bash
   \$ make test
   ```

10. Install additional `VSCode Extensions` to enable, within a single `VSCode` Window,
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

Note: This setup has been tested on a MacBookPro with

* MacOSX Ventura v13.2.1,
* Docker v20.10.23, build 7155243, and
* VSCode v1.76.2 (Universal)
* python v3.8.2

## GitHub Configuration

1. The main branch has name `main` rather than `master` or `trunk`, and there is a
   `pages` branch for GitHub Actions deployment of GitHub Pages documenation
2. Under Settings, `Environment` and `Pages` have been configured to enable
   `Build and deployment` of documentation with `GitHub Actions`.  See
   [GitHub Pages docs](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)
3. Under Settings, `Branches` has been configured with
   * `Branch protection rule` with `[mp][a]*[ie][ns]` pasted into
     `Branch pattern name`, applying the protection rule to branches `main` and `pages`
   * `Protect matching branches` rules check
     * `Require a pull request before merging`
     * `Require conversation resolution before merging`
     * `Do not allow bypassing the above settings`

## Legal Notice

When contributing to this project, you must agree that you have authored 100% of the
content, that you have the necessary rights to the content and that the content you
contribute may be provided under the project license.
