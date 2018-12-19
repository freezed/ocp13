#### Développeur d'application Python - Projet final

_**Note** : La version livrée de ce document est disponible [à cette adresse][readme]._

[![Build Status](https://www.travis-ci.org/freezed/ocp13.svg?branch=master)](https://www.travis-ci.org/freezed/ocp13)
[![Coverage Status](https://coveralls.io/repos/github/freezed/ocp13/badge.svg?branch=master)](https://coveralls.io/github/freezed/ocp13?branch=master)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/freezed/ocp13.svg)](http://isitmaintained.com/project/freezed/ocp13 "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/freezed/ocp13.svg)](http://isitmaintained.com/project/freezed/ocp13 "Percentage of issues still open")

# Note d'intention

## Contexte _pédagogique_

Après avoir réalisé, entre autre, [un jeu en 2D][p3], [un chat-bot][p5] et [un outil de recherche d'aliments de substitution][p11] explorant notamment l'écosystème [Python][wikipython], le [TDD][wikitdd] ou l'[Intégration continue][wikici], me voici enfin arrivé à la dernière étape du parcours _[développeur·se d'application Python][dapy]_ : développer un projet _libre_ avec une _portée sociale_.

> Menez un projet numérique de la forme qui vous semblera la plus adaptée pour répondre à un besoin autour de vous. Il peut s’agir d’un site de réservation pour l’association de théâtre de votre ville, d’une application pour localiser et référencer les objets trouvés pendant un festival, etc. Prenez le temps de choisir un sujet qui vous touche et pour lequel vous ressentez un véritable besoin.

# Le projet

## Contexte _utilisateur_

[Valérie](https://refuge.la-cordee.net/users/3271) et [Serge][serge] sont travailleurs indépendants (les `utilisateurs` dans la suite du doc.). Nous nous [rencontrons][refuge] à _Lyon_ dans la [communauté de travail][cordee] que nous fréquentons. Pour leurs activités respectives ils sont à la recherche d'un outil qui leur permettrait de gérer aisément leur _réseau de contacts_ : prospection, suivi, opportunités etc.

Bien qu'aillant chacun des activités (_très_) différentes, après une écoute de leurs problématiques respectives, un certain nombre de leurs besoins sont similaires et sont compatibles avec un outil commun. En plus il pourrait même convenir à d'autres indépendants de cette _communauté de travail_ ou d'une autre!

## Spécifications

* service en ligne ([SaaS][wikisaas]), en gardant à l'esprit qu'un usage _hors réseau_ sera certainement implémenté à l'avenir
* les données seront réparties dans différents _«objets»_ :
    - des `contacts` auxquels seront associés des `affaires`
    - aux `affaires` et `contacts` pourront être associés à des `notes`
    - des `étiquettes` permettront une organisation souple et transversale de ces informations en s'associant à tout ou partie des objets définis ci dessus. Une étiquette pourrait représenter : un _groupe de contact_, une _entreprise_, un _secteur professionnel_, un _statut_, etc.
* les `contacts` seront cloisonnés à l'`utilisateur` qui les aura créés, en gardant à l'esprit qu'un partage des `contacts` entre les `utilisateurs` du service sera implémenté à l'avenir
* import de `contacts` existant :
    - individuel (formulaire)
    - en lot, préférence pour les formats [Vcard][wikivcf] et/ou [CSV][wikicsv]
    - connection à un serveur [CardDAV][wikidav]

### Modèle de données simplifié

![Domaine fonctionnel simplifié][lfd]


## Livrables attendus

* Une [note d’intention][readme] expliquant les objectifs du projet.
* Un [bilan de votre expérience][bilan] sur ce projet.
* [Document détaillant votre implémentation][approach] des 12 bonnes pratiques de l’[_extreme programming_][wikixtrem].
* Lien vers votre [tableau agile][kanban]
* Lien vers votre [projet déployé][ocp13]
* Un [support de présentation][pitch]


[approach]: https://github.com/freezed/ocp13/blob/v1.0/doc/approach.md
[bilan]: https://github.com/freezed/ocp13/blob/v1.0/doc/bilan.md
[cordee]: https://www.la-cordee.net/
[dapy]: https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python "Maîtrisez Python, le langage des startups et des scientifiques, pour réaliser vos propres applications web"
[kanban]: https://github.com/freezed/ocp13/projects/1
[lfd]: https://raw.githubusercontent.com/freezed/ocp13/v1.0/doc/data_model/functional_model_light.png
[ocp13]: ocp13-1664.herokuapp.com
[p11]: https://github.com/freezed/ocp8/blob/v0.3/README.md#contexte
[p3]: https://github.com/freezed/ocp3/#pydev-projet-3
[p5]: https://github.com/freezed/ocp5#pydev-projet-5
[pitch] :https://gitpitch.com/freezed/ocp13/v0.1?p=doc
[readme]: https://github.com/freezed/ocp13/blob/v1.0/README.md#note-dintention
[refuge]: https://refuge.la-cordee.net/messages/5733
[serge]: https://refuge.la-cordee.net/users/2579
[wikici]: https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue "Lien vers la page «Intégration continue» sur wikipedia"
[wikicsv]: https://fr.wikipedia.org/wiki/Comma-separated_values "Lien vers la page «Comma-separated_values» sur Wikipedia"
[wikidav]: https://fr.wikipedia.org/wiki/CardDAV "Lien vers la page «CardDAV» sur Wikipedia"
[wikipython]: https://fr.wikipedia.org/wiki/Python_(langage) "Lien vers la page «Python (langage)» sur wikipedia"
[wikisaas]: https://fr.wikipedia.org/wiki/Logiciel_en_tant_que_service "Lien vers la page «Logiciel en tant que service» sur wikipedia"
[wikitdd]: https://fr.wikipedia.org/wiki/Test_driven_development "Lien vers la page «Test driven development» sur wikipedia"
[wikivcf]: https://fr.wikipedia.org/wiki/VCard "Lien vers la page «VCard» sur Wikipedia"
[wikixtrem]: https://fr.wikipedia.org/wiki/Extreme_programming "Lien vers la page «Extreme programming» sur Wikipedia"
