# ToDoList

## Validated specifications

* [x] [1][1]: Basic Django Hello-World
* [x] [2][2]: Set-up Heroku staging environnement
    - [x] `Procfile`
    - [x] `settings.py`
    - [x] `gunicorn`
    - [x] `ENV_VARS`
* [x] [3][3]: Set-up Sentry
* [x] [4][4]: Set-up travis
* [x] [13][13]: Add connection to a coverage service
* [x] [8][8]: Define physical data model
* [x] [6][6]: Configure statics
    - [x] `static/favico.ico` (requested by browsers)
    - [x] devel env
    - [x] heroku local
    - [x] heroku
* [x] [7][7]: Use knacss HTML/CSS template
    - [x] `home.html`
    - [x] `about.html`
    - [x] `404.html` & `500.html`
    - [x] footer
    - [x] header
* [x] [9][9]: Postgres config
* [x] [11][11]: Add authentification (a14n) pages
    - [x] signup
    - [x] logout
    - [x] login
* [ ] [14][14] User account page
    - [ ] update personnal info
    - [ ] contact list access
    - [ ] next deadline
    - [ ] last entry
* [ ] [10][10]: create `app.models`
* [ ] [15][15] Add CRUD contacts page
    - [ ] Create
    - [ ] Read
    - [ ] Update
    - [ ] Delete
* [ ] [5][5]: Define template grid
* [ ] [16][16] Import contacts via
    - [ ] a CSV file
    - [ ] Vcard file
    - [ ] WebDAV server
    - https://github.com/l0b0/vcard
    - https://github.com/python-caldav/caldav
    - https://github.com/eventable/vobject
* [ ] [12][12]: Set-up production environnement

## Candidates specifications

* Associate a todolist to a contact
* Todolist entry have deadlines
* List associated objects by date
* contacts views : 
    - all my contacts (filtered on attributes)
    - list of contacts with associated business
    - list of actions in progress (not flagged "done")
    - list of all ongoing actions
    - list of all ongoing jobs :
        * default: pending jobs
        * other: all jobs, jobs with actions coming…
* Add note to contacts
* Add deal to contacts
* Add tag
* Use paginator in contact list

[1]: https://github.com/freezed/ocp13/issues/1
[2]: https://github.com/freezed/ocp13/issues/2
[3]: https://github.com/freezed/ocp13/issues/3
[4]: https://github.com/freezed/ocp13/issues/4
[5]: https://github.com/freezed/ocp13/issues/5
[6]: https://github.com/freezed/ocp13/issues/6
[7]: https://github.com/freezed/ocp13/issues/7
[8]: https://github.com/freezed/ocp13/issues/8
[9]: https://github.com/freezed/ocp13/issues/9
[10]: https://github.com/freezed/ocp13/issues/10
[11]: https://github.com/freezed/ocp13/issues/11
[12]: https://github.com/freezed/ocp13/issues/12
[13]: https://github.com/freezed/ocp13/issues/13
[14]: https://github.com/freezed/ocp13/issues/14
[15]: https://github.com/freezed/ocp13/issues/15
[16]: https://github.com/freezed/ocp13/issues/16
