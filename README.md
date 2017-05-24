[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

# Twitter Monitor

This project was built using the [Django React Boilerplate](https://github.com/vintasoftware/django-react-boilerplate).

### How to test `django-admin startproject`

If you made changes to this boilerplate and want to test them, commit your changes and use `git archive -o boilerplate.zip HEAD` to create the template zip.

### How to test Heroku deployment

Push your changes to a branch and visit `https://dashboard.heroku.com/new?template=https://github.com/fill-org-or-user/fill-project-repo-name/tree/fill-branch` (replace all `fill`).

### How to add a 'Deploy to Heroku' button

Read [this](https://devcenter.heroku.com/articles/heroku-button#adding-the-heroku-button).

p.s. if you want to deploy in a different way please take a look the `app.json` file for what needs to be configured.

## Developing

### Quickstart

- Create a copy of ``{{project_name}}/settings/local.py.example`` in ``{{project_name}}/settings/local.py``
- Create a ``.env`` file in the root of the project and add ``DJANGO_SETTINGS_MODULE="{{project_name}}.settings.local"`` to it
- Create the migrations for `users` app: `python manage.py makemigrations`
- Run the migrations: `python manage.py migrate`

### Tools

- Setup [editorconfig](http://editorconfig.org/), [flake8](http://flake8.pycqa.org/en/latest/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Running the project

- `pip install -r requirements.txt`
- `npm install`
- `make bundle`
- `python manage.py runserver`

### Testing

`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs

Add high level dependecies to `requirements-to-freeze.txt` and `pip freeze > requirements.txt`. This is [A Better Pip Workflow](http://www.kennethreitz.org/essays/a-better-pip-workflow).

## Checking lint

- Manually with `flake8` and `npm run lint` on project root.
- During development with an editor compatible with flake8 and ESLint.

## Pre-commit hooks

- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.
