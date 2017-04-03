# __CONSIGNES DE DEVELOPPEMENT__

## Rôles
- Chef Projet : Mathieu Pubert
- Intégrateur global : Mathieu Pubert
- Documentaliste Projet : A définir

- Module Questionnaire :
  - Intégrateur Module :
  - Documentaliste Module :


- Module Analyse :
  - Intégrateur Module :
  - Documentaliste Module :


- Module Sondage :
  - Intégrateur Module :
  - Documentaliste Module :


- Module Serveur :
  - Intégrateur Module :
  - Documentaliste Module :


## Procédure de développement

Le développement au cous du projet se fera selon le principe des API:

1. On ne change pas le code du camarade.

    Il existe un outil sur Gitlab permettant de "blâmer" une portion de code non conforme et de proposer une solution au développeur responsable. Au pire, il y a le Slack du projet, les e-mails, les téléphones etc...

2.  On ne change pas le code du camarade !

    Si le camarade se montre réticent alors que vos propositions sont raisonnables. On en parle au chef de projet. Si le chef de projet n'est pas réceptif, on en parle au tuteur.

3. Quand on prend un item du backlog , on le note sur le BACKLOG et on renseigne son avancement.


## Procédure de versionnage

Les opérations de versionnage se feront comme suit :

- Integrateur Global :
  - Forke le dépot du groupe et le remote,
  - Intègre les modules au projet
  - Propose les merge request au depot du groupe

- Intégrateur Module :
  - Forke le projet du groupe et le remote,
  - Intègre les développements du module
  - Commit son code sur __son__ origin, pioche sur l'origin de  l'intégrateur global
  - Propose les merge request au depot de L'intégrateur global

- Développeur :  
  - Forke le projet de l'intégrateur module et le remote,
  - Commit son code sur __son__ origin, pioche sur l'origin de  l'intégrateur module
  - Propose les merge request au depot de L'intégrateur module


## Documentation

#### Documentation du code

La documentation du code sera de la responsabilité de chaque développeur :

###### Sur chaque fichier, de la documentation ressemblant a ce modèle :

Pour python
```python
########################################################
#MONFICHIER.py
#Auteur(s) : Bob, Alice
#
# Description sommaire du contenu du fichier
#
########################################################

class MaClasse():
  """
  Description de la classe
  @attribut a1: Type, sémantique de l'attribut
  @method m1: profil de la méthode (ex : mafonction(p1,p2))
  """

  def mafonction(p1,p2):
  """
  Description de l'effet de la fonction
  @param p1: Type, contenu attendu du parametre
  @param p2: Type, contenu attendu du parametre
  @return : Type, sémantique du retour de la fonction
  """
    res=False
    return res
```

pour javascript ou php
```javascript
/** MONFICHIER.js
  * Auteur(s) : Bob, Alice
  *
  * Description sommaire du contenu du fichier
  *
  */


  class MaClasse {
    /**
      * Description de la classe
      * @attribut a1: Type, sémantique de l'attribut
      * @method m1: profil de la méthode (ex : mafonction(p1,p2))
      */



      /** Description de la méthode
        * @param p1: Type, contenu attendu du parametre
        * @param p2: Type, contenu attendu du parametre
        * @return : Type, sémantique du retour de la fonction
        */
      mafonction(p1, p2) {
        var res=false
        return res
      }
  }



```
#### Documentation des modules

Dans chaque binôme, un développeur sera volontaire, ou désigné volontaire si il n'y en a pas au moment du développement, pou être redacteur d'une fiche de documentation (MonModule_doc.md) du module expliquant :
- Comment l'intégrer au projet (chemin des fichiers etc...).
- Les contributeurs au module
- la structure globale


### Allure du BACKLOG
L'application sera divisée en 4 modules:

## Un module
- Dev1
- Dev2


#### Programme
###### Code
1. __[Etat: EN COURS (Prénom Dev1)]__ Description Item
2. __[Etat: ATTENTE]__ Description Item

###### Interface
1. __[Etat: FAIT (Prénom Dev2)]__ Description Item
2. __[Etat: ATTENTE]__ Description Item

#### Documentation
- __[Etat: ATTENTE]__ Description Item
