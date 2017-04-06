create table TYPE_UTILISATEUR(
	id_typeutil SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_typeutil VARCHAR(20) NOT NULL,
	PRIMARY KEY (id_typeutil)
);

create table UTILISATEUR (
	id_utilisateur SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,  
	nom_utilisateur VARCHAR(20) NOT NULL, 
	prenom_utilisateur VARCHAR(20),
	login_utilisateur VARCHAR(20) NOT NULL, 
	password_utilisateur VARCHAR(20) NOT NULL, 
	id_typeutil SMALLINT UNSIGNED, 
	PRIMARY KEY (id_utilisateur),
	FOREIGN KEY (id_typeutil) REFERENCES TYPE_UTILISATEUR(id_typeutil)
	
	
);


create table SONDE (
	id_sonde SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	nom_sonde VARCHAR(20) NOT NULL, 
	prenom_sonde VARCHAR(20) NOT NULL, 
	sexe_sonde VARCHAR(20) NOT NULL, 
	datenaiss_sonde DATE, 
	tel_sonde VARCHAR(14)
	id_csp SMALLINT UNSIGNED,
	id_adresse SMALLINT UNSIGNED,
	PRIMARY KEY (id_sonde),
	FOREIGN KEY (id_csp) REFERENCES CSP(id_csp),
	FOREIGN KEY (id_adresse) REFERENCES ADRESSE(id_adresse)
);

create table QUESTIONNAIRE (
	id_questionnaire SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_questionnaire VARCHAR(100) NOT NULL, 
	dateheurelim_questionnaire DATE, 
	accessible_questionnaire BOOLEAN, 
	termine_questionnaire BOOLEAN, 
	analyse_questionnaire BOOLEAN,
	dateheure_creation DATE, 
	url_analyse VARCHAR(100),  
	id_utilisateur SMALLINT UNSIGNED, 
	id_panel SMALLINT UNSIGNED, 
	id_entreprise SMALLINT UNSIGNED,
	FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
	FOREIGN KEY (id_panel) REFERENCES PANEL(id_panel),
	FOREIGN KEY (id_entreprise) REFERENCES ENREPRISE(id_entreprise),
	PRIMARY KEY (id_questionnaire)
);

create table REMPLIR(
	id_sonde SMALLINT UNSIGNED, 
	id_questionnaire SMALLINT UNSIGNED,
	id_utilisateur SMALLINT UNSIGNED,
	date_remplissage DATE NOT NULL,
	PRIMARY KEY (id_sonde),
	PRIMARY KEY (id_questionnaire),
	FOREIGN KEY (id_sonde) REFERENCES SONDE(id_sonde),
	FOREIGN KEY (id_questionnaire) REFERENCES QUESTIONNAIRE(id_questionnaire),
	FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur)

);

create table ANALYSER(
	id_questionnaire SMALLINT UNSIGNED,
	id_utilisateur SMALLINT UNSIGNED,
	date_analyse DATE NOT NULL,
	url_analyse VARCHAR(100),
	PRIMARY KEY (id_utilisateur),
	PRIMARY KEY (id_questionnaire),
	PRIMARY KEY (date_analyse),
	FOREIGN KEY (id_questionnaire) REFERENCES QUESTIONNAIRE(id_questionnaire),
	FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur)

);


create table VILLE (
	codeinsee_ville VARCHAR(5) NOT NULL, 
	nom_ville VARCHAR(50), 
	codepostal_ville VARCHAR(5),
	PRIMARY KEY(codeinsee_ville)
);

create table CSP (
	id_csp SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_csp VARCHAR(100),
	PRIMARY KEY(id_csp)
);


create table APPARTENIR (
	id_panel SMALLINT UNSIGNED , 
	id_sonde SMALLINT UNSIGNED,
	PRIMARY KEY (id_panel),
	PRIMARY KEY (id_sonde),
	FOREIGN KEY (id_panel) REFERENCES PANEL(_id_panel_),
	FOREIGN KEY (id_sonde) REFERENCES SONDE(_id_sonde_)
);

create table ADRESSE (
	id_adresse SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	numero_adresse INTEGER(10), 
	bister_adresse VARCHAR(3), 
	libellevoie_adresse VARCHAR(150), 
	batiment_adresse VARCHAR(5), 
	etage_adresse VARCHAR(3), 
	escalier_adresse VARCHAR(2), 
	appartement_adresse VARCHAR(10), 
	codeinsee_ville VARCHAR(5),
	PRIMARY KEY (id_adresse),
	FOREIGN KEY (codeinsee_ville) REFERENCES VILLE(codeinsee_ville)

);

create table CHOIX_MULTIPLE (
	id_choixmul SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_choixmul VARCHAR(100), 
	id_question SMALLINT UNSIGNED,
	PRIMARY KEY (id_choixmul),
	FOREIGN KEY (id_question) REFERENCES QUESTION(id_question)
);

create table PANEL (
	id_panel SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_panel VARCHAR(100),
	PRIMARY KEY (intitule_panel)
);

create table QUESTION (
	id_question SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	enonce_question VARCHAR(100), 
	urlanal_question VARCHAR(100), 
	id_typequest SMALLINT UNSIGNED, 
	id_questionnaire SMALLINT UNSIGNED,
	PRIMARY KEY (id_question),
	FOREIGN KEY (id_typequest) REFERENCES TYPE_QUESTION(id_typequest),
	FOREIGN KEY (id_questionnaire) REFERENCES QUESTIONNAIRE(id_questionnaire)
);



create table ENTREPRISE (
	id_entreprise SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	nom_entreprise VARCHAR(100) NOT NULL, 
	tel_entreprise VARCHAR(14), 
	email_entreprise VARCHAR(133), 
	id_adresse SMALLINT UNSIGNED,
	PRIMARY KEY (id_entreprise),
	FOREIGN KEY (id_adresse) REFERENCES ADRESSE(id_adresse)
);

create table TYPE_QUESTION (
	id_typequest SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_typequest VARCHAR(10),
	PRIMARY KEY (id_typequest)
);

create table ENREGISTRER_NOTE (
	id_question SMALLINT UNSIGNED, 
	dateheure_note DATE NOT NULL, 
	note VARCHAR (5),
	PRIMARY KEY(id_question),
	PRIMARY KEY(dateheure_note),
	FOREIGN KEY(id_question) REFERENCES QUESTION(id_question)
)

create table ENREGISTRER_REPONSE (
	id_question SMALLINT UNSIGNED, 
	dateheure_reponse DATE NOT NULL, 
	commentaire VARCHAR (140),
	PRIMARY KEY(id_question),
	PRIMARY KEY(dateheure_reponse),
	FOREIGN KEY(id_question) REFERENCES QUESTION(id_question)
)


create table ENREGISTRER_CHOIX (
	id_question SMALLINT UNSIGNED, 
	dateheure_choix DATE NOT NULL, 
	id_choixmul SMALLINT UNSIGNED,
	PRIMARY KEY(id_question),
	PRIMARY KEY(dateheure_choix),
	FOREIGN KEY(id_question) REFERENCES QUESTION(id_question),
	FOREIGN KEY(id_choixmul) REFERENCES CHOIX_MULTIPLE(id_choixmul)
)


create table ENREGISTRER_CLASSEMENT (
	id_question SMALLINT UNSIGNED, 
	dateheure_classement DATE NOT NULL, 
	id_choixmul SMALLINT UNSIGNED,
	position VARCHAR(2),
	PRIMARY KEY(id_question),
	PRIMARY KEY(dateheure_classement),
	PRIMARY KEY(id_choixmul),
	FOREIGN KEY(id_question) REFERENCES QUESTION(id_question),
	FOREIGN KEY(id_choixmul) REFERENCES CHOIX_MULTIPLE(id_choixmul)
);

create table ENREGISTRER_SELECTION(
	id_question SMALLINT UNSIGNED, 
	dateheure_selection DATE NOT NULL, 
	id_choixmul SMALLINT UNSIGNED,
	PRIMARY KEY(id_question),
	PRIMARY KEY(dateheure_selection),
	PRIMARY KEY(id_choixmul),
	FOREIGN KEY(id_question) REFERENCES QUESTION(id_question),
	FOREIGN KEY(id_choixmul) REFERENCES CHOIX_MULTIPLE(id_choixmul)

);










