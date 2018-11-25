Documentation
=============

**Note** : _Check latest version of this doc on [github][doc]._

---

## Dependencies

- `django 2.1.4`
- `psycopg2-binary 2.7.6.1`
- `python 3.6.6`

## Dependencies for [Heroku][heroku] running

- `dj-database-url 0.5.0`
- `gunicorn 19.9.0`
- `whitenoise 4.1.2`
    - `heroku/7.19.3 linux-x64 node-v11.3.0`
    - with `gunicorn 19.9.0`


## Development tools used

- `coverage 4.5.2`
- `pytest 4.0.1`
- `pytest-cov 2.6.0`
- `pytest-django 3.4.4`
- `python-coveralls`
- `sentry-sdk 0.5.5`

## Installation

1. get the code : `git clone git@github.com:freezed/ocp13.git`
2. create a dedicated virtualenv : `python3 -m venv .venv`
3. starts virtualenv  : `source .venv/bin/activate`
4. adds dependencies : `cd ocp13; pip install -r requirements.txt`
5. creates a `postgresql` DB
6. Edit [`core/settings.py`][settings]
7. set DB : `./manage.py migrate`
8. run tests : `pytest --cov=a14n --cov=core --cov=user --cov=lead`
9. run developement server : `./manage.py runserver`

## File organisation

#### Django project name

- **core**

#### Django apps

- **a14n** : Authentification
- **lead** : Contacts management
- **log** : Entries attached to a contact
- **user** : User account management

#### Project tree

```shell
├── manage.py
├── Procfile
├── pytest.ini
├── README.md
├── requirements.txt
├── staticfiles
│   └── […]
├── doc
│   ├── approach.md
│   ├── data_model
│   │   └── […]
│   ├── documentation.md
│   ├── img
│   └── TODOlist.md
├── core
│   ├── settings
│   │   ├── heroku_local.py
│   │   ├── __init__.py
│   │   ├── staging.py
│   │   └── travis.py
│   ├── static
│   │   ├── css
│   │   ├── favico.ico
│   │   └── img
│   ├── templates
│   │   ├── 403.html
│   │   ├── […]
│   │   └── home.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── a14n
│   ├── apps.py
│   ├── templates
│   │   ├── a14n
│   │   └── registration
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── lead
│   ├── apps.py
│   ├── fixtures
│   │   └── lead_data.json
│   ├── forms.py
│   ├── migrations
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── templates
│   │   └── lead
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── log
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── templates
│   │   └── log
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── user
    ├── apps.py
    ├── forms.py
    ├── templates
    │   ├── auth
    │   └── user
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Data model

Table `user` model is from built-in django authentification module, packages are _Django apps_ :

![PMD image](https://raw.githubusercontent.com/freezed/ocp13/master/doc/data_model/functional_model.png)

[PUML sources](https://github.com/freezed/ocp13/blob/master/doc/data_model/functional_model.puml)


[doc]: https://github.com/freezed/ocp13/blob/master/doc/documentation.md
[heroku]: https://heroku.com
[settings]: https://github.com/freezed/ocp13/blob/master/omega/settings.py#L84
