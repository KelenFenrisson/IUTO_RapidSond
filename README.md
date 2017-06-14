# Projet Tutoré : Rapid'Sond

## Description

Cette application est le fruit du travail d'un groupe d'étudiants du département Informatique l'IUT d'Orléans (Groupe-ASA) d'après un sujet de projet tutoré, disponible dans /doc.



## Installation

#### Partie Client

Prérequis : Votre machine doit êter capable d'héberger une application web

1. Copier le dossier /client et son contenu sur un serveur web. Vous pouvez le renommer comme vous le souhaitez.

2.

#### Partie Serveur

Prerequis : Votre machine doit êter capable d'heberger une application Flask (Serveur VPS)

1. Copier le dossier REST et son contenu sur le serveur

2. Créer un virtualenv
``` bash
login@machine ~/mon/chemin/serveur/ $ virtualenv -p python3 venv
```

3. Activer ce venv

``` bash
login@machine ~$ source ~/mon/chemin/venv/bin/activate
```


4. Mettre a jour les modules du venv

``` bash
(venv)login@machine ~/mon/chemin/REST/ $ pip install -r pip-requirements.txt
```

5. Créer un fichier db_credentials.py dans REST/sondages/ contenant :

``` python
MYSQL_SERVER = "ipserveur:port"
MYSQL_DATABASE = "nom_basededonnees"
MYSQL_LOGIN = "login_mysql"
MYSQL_PASSWORD = "password_mysql"
```

6. Creer les tables de la base de données

``` bash
(venv)login@machine ~/mon/chemin/REST/ $ ./manage.py syncdb
```

Un jeu d'essai pour la base de données est diponible dans REST/sondages/jeu_essai.sql.
Dans mysql :


``` mysql
mysql > source jeu_essai.sql
```



7. Lancer le serveur (dans l'exemple , le serveur est lançé sur 127.0.0.1:5000)

``` bash
(venv)login@machine ~/mon/chemin/REST/ $ ./manage.py runserver -h 127.0.0.1 -p 5000
```

## Documentation


## Projet

- Integrateur principal: Mathieu
- Developpeurs : Mathieu, Julien, Jérémie, Leo, Olivier, Roméo



#### Base de données
- Conception, script de création et jeu d'essai: Mr LIMET



## Module client Onepage

- Integrateur principal : Julien
- Developpeurs : Julien, Leo, Olivier, Jeremie, Roméo

#### Programme

Une application web onepage permettant de concevoir des questionnaires et d'interroger des sondés.
Le développement d'une partie analyse statistique

###### Code

- Javascript, JQuery(Ajax), HTML/CSS(BootStrap)

###### Interface

- Maquettage issu du projet MyBalsamiq de conception d'interfaces : https://infoiut45.mybalsamiq.com/projects/sondasa/grid



## Module serveur REST

- Integrateur : Mathieu
- Developpeur : Mathieu

#### Programme

Un serveur REST développé en python (Flask-Restless), alimenté par une base de données mysql

###### Code

Principalement du python3, un peu de html/CSS

###### Interface

- home (/) : contient une description sommaire de l'API REST et des entités manipulables

