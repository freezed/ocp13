# TODOlist

## Validated specifications

* [x] [~1. Basic Django Hello-World~][1] :
* [x] [~2. Set-up Heroku staging environnement~][2] :
    - [x] ~`Procfile`~
    - [x] ~`settings.py`~
    - [x] ~`gunicorn`~
    - [x] ~`ENV_VARS`~
* [x] [~3. Set-up Sentry~][3] :
* [x] [~4. Set-up travis~][4] :
* [x] [~13. Add connection to a coverage service~][13] :
* [x] [~8. Define physical data model~][8] :
* [x] [~6. Configure statics~][6] :
    - [x] ~`static/favico.ico` (requested by browsers)~
    - [x] ~devel env~
    - [x] ~heroku local~
    - [x] ~heroku~
* [x] [~7. Use knacss HTML/CSS template~][7] :
    - [x] ~`home.html`~
    - [x] ~`about.html`~
    - [x] ~`404.html` & `500.html`~
    - [x] ~footer~
    - [x] ~header~
* [x] [~9. Postgres config~][9] :
* [x] [~11. Add `a14n` app (authentification)~][11] :
    - [x] ~signup~
    - [x] ~logout~
    - [x] ~login~
* [ ] [14 Add `user` app (account)][14] :
    - [x] ~index page~
    - [x] ~show personnal info~
    - [ ] update personnal info
    - [ ] `lead` list access
    - [ ] next deadline
    - [ ] last entry
* [ ] [~10. Add `lead` app (contact)~][10] :
    - [x] ~1st test, view & template~
    - [x] ~models.py` (contact)~
    - [x] ~Create~
    - [x] ~Read~
    - [x] ~Update~
    - [x] ~Delete~
* [ ] [21. Add `log` app (entry)][21] :
    - [ ] 1st test, view & template
    - [ ] `models.py` (entry)
    - [ ] Create
    - [ ] Read
    - [ ] Update
    - [ ] Delete
* [ ] [15. Add `tag` app (label)][15] :
    - [ ] 1st test, view & template
    - [ ] `models.py` (label)
    - [ ] Create
    - [ ] Read
    - [ ] Update
    - [ ] Delete
    - [ ] Associate with `contact`
    - [ ] Associate with `entry`
* [ ] [16 Import contacts via][16] :
    - [ ] a CSV file
    - [ ] Vcard file
    - [ ] WebDAV server
    - https.//github.com/l0b0/vcard
    - https.//github.com/python-caldav/caldav
    - https.//github.com/eventable/vobject
* [ ] [5. Define template grid][5] :
* [ ] [12. Set-up production environnement][12] :

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
[21]: https://github.com/freezed/ocp13/issues/21
