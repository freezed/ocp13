# [DAPY Projet 13]

_ 20 décembre 2018 _

![](/doc/img/coveralls-r.png)
![](/doc/img/django-r.png)
![](/doc/img/github-r.png)
![](/doc/img/heroku-r.png)
![](/doc/img/knacss-r.png)
![](/doc/img/openclassrooms-r.png)
![](/doc/img/papertrail-r.png)
![](/doc/img/py-r.png)
![](/doc/img/sentry-r.png)
![](/doc/img/stackoverflow-r.png)
![](/doc/img/travisf-r.png)

---

#  Contexte

@ul
* 12 mois de `py.mmersion` !
* Comme les pro !
* Une photo du décollage !
@ulend

---

# Approche ?

+++

## Des clients !

![](/doc/img/lacordee.png)
![](/doc/img/clients.png)

+++

## Des besoins !

@ul
* Carnet d'adresse et …
* y associer des notes, rappels, listes, _foobar_
@ulend

---

# La méthode ?

+++

### Agile !

@ul
* Comme _tout le monde_ … ?
@ulend

+++

### Décomposition fonctionnelle

![](/doc/img/decofon.png)

+++

### Modélisation des données

+++

![PDM image](/doc/data_model/physical_data_model.png)

---

# Des outils ?

+++

### Plannification !

![](/doc/img/kanban.png)

+++

### Livraison/Déploiement continue

![Staging CI/CD flow - image](/doc/img/travis.jpg)

+++

### Des échanges brefs mais réguliers

![](/doc/img/mail-list.jpg)
![](/doc/img/mail-detail.jpg)

+++

## Réitération

@ul
- quotidienne
- à chaque retour client
@ulend

---

# Du code ?

![](/doc/img/git.png)

+++

#### Des tests, des tests : plein de tests!

Objectif 100%

![](/doc/img/coveralls.png)

+++

`from pytest import parametrize`

![](/doc/img/log-test1.png)

+++

`from pytest import fixture`

![](/doc/img/log-test2.png)

+++

`pytest.do_magik()`

![](/doc/img/log-test3.png)

+++

### Chaînage d'URLs

![](/doc/img/chained-app-url.png)


+++

### Class Based View

@ul
- … ou la puissance des objets
@ulend

+++

_Vues de base_ : (presque) rien à faire !

![](/doc/img/core-urls.png)

+++

_Vues génériques_ : déballez, utilisez !

![](/doc/img/lead-view.png)

+++

_Vues génériques_ : les joies de la surcharge 1/3

![](/doc/img/log-view1.png)

+++

_Vues génériques_ : les joies de la surcharge 2/3

![](/doc/img/log-view2.png)

+++

_Vues génériques_ :les joies de la surcharge 3/3

![](/doc/img/log-view3.png)

+++

_En `Form`_ ?

![](/doc/img/entryform1.png)

+++

_En `Form`_ ?

![](/doc/img/entryform2.png)

---

# Les temps forts

@ul
* Le découpage du modèle de donnée en application Django
* Un _vrai_ projet qui démarre en _TDD_
* La couverture de test à 100%
@ulend

---

### `from __future__ import ideas`

@ul
* Création de l'app `tag`
* Import des contacts
* Connection `webDAV`
* Refactoriser les tests (fixtures _Django_, …)
* … et peut être un peut de _front_
@ulend


---

### C'est fini : merci !


` \m/_(^_^)_\m/ `

![](/doc/img/coveralls-r.png)
![](/doc/img/django-r.png)
![](/doc/img/github-r.png)
![](/doc/img/heroku-r.png)
![](/doc/img/knacss-r.png)
![](/doc/img/openclassrooms-r.png)
![](/doc/img/papertrail-r.png)
![](/doc/img/py-r.png)
![](/doc/img/sentry-r.png)
![](/doc/img/stackoverflow-r.png)
![](/doc/img/travisf-r.png)
