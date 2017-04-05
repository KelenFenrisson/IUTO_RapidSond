# MLD du projet

## Description des tables :

**En gras** : clé primaire

En italique : clé étrangère

***En gras et italique*** : clé étrangère et primaire


TYPE_QUESTION ( **id_typequest**, libelle_typequest )


TYPE_UTILISATEUR ( **id_typeutil**, libelle_typeutil )


CSP ( **id_csp**, libelle_csp )


PANEL ( **id_panel**, intitule_panel )


VILLE ( **codeinsee_ville**, nom_ville, codepostal_ville )


ADRESSE ( **id_adresse**, numero_adresse, bister_adresse, libellevoie_adresse, batiment_adresse, etage_adresse, escalier_adresse, appartement_adresse, *codeinsee_ville* )


ENTREPRISE ( **id_entreprise**, nom_entreprise, tel_entreprise, email_entreprise, *id_adresse* )


SONDE ( **id_sonde**, nom_sonde, prenom_sonde, sexe_sonde, datenaiss_sonde, tel_sonde, *id_csp*, *id_adresse* )


QUESTIONNAIRE ( **id_questionnaire**, intitule_questionnaire, dateheurelim_questionnaire, accessible_questionnaire, termine_questionnaire, *id_entreprise*, *id_panel*, analyse_questionnaire, *id_utilisateur*, dateheure_creation )


QUESTION ( **id_question**, enonce_question, urlanal_question, *id_typequest*, *id_questionnaire* )


CHOIX_MULTIPLE ( **id_choixmul**, intitule_choixmul, *id_question* )


UTILISATEUR ( **id_utilisateur**, nom_utilisateur, prenom_utilisateur, login_utilisateur, password_utilisateur, *id_typeutil* )



APPARTENIR ( ***id_panel***, ***id_sonde*** )


REMPLIR ( ***id_sonde***, ***id_questionnaire***, *id_utilisateur*, date )


ANALYSER ( ***id_utilisateur***, ***id_questionnaire***, **date_analyse**, url_analyse )


ENREGISTRER_CHOIX ( ***id_question***, **dateheure_choix**, *id_choixmul* )


ENREGISTRER_CLASSEMENT ( ***id_question***, **dateheure_classement**, ***id_choixmul***, position )


ENREGISTRER_NOTE ( ***id_question***, **dateheure_note**, note )


ENREGISTRER_REPONSE ( ***id_question***, **dateheure_reponse**, commentaire )


ENREGISTRER_SELECTION ( ***id_question***, **dateheure_selection**, *id_choixmul* )
