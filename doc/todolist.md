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
* [ ] [7][7]: Use knacss CSS framework
    - [ ] home
    - [ ] footer
    - [ ] header
    - [ ] about
    - [ ] 404/500 error
* [ ] [6][6]: Configure statics
* [ ] [9][9]: Postgres config
* [ ] [10][10]: create `app.models`
* [ ] [11][11]: Add auth pages
    - [ ] sign-up
    - [ ] logout
    - [ ] login
* [ ] [5][5]: Define template grid
* [ ] [12][12]: Set-up production environnement

## Candidates specifications

* Add account page
* Add CRUD contacts page
    - Import contacts via Vcard file
* https://github.com/l0b0/vcard
    - Import contacts via a WebDAV server
    - https://github.com/python-caldav/caldav
    - https://github.com/eventable/vobject
* Import contacts via a CSV file
* Add user/contact pages
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
