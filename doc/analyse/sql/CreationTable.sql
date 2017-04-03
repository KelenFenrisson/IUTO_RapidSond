create table TYPE_UTILISATEUR(
	id_typeutil_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_typeutil VARCHAR(20) NOT NULL,
	PRIMARY KEY (id_typeutil_)
);

create table UTILISATEUR (
	_id_utilisateur_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,  
	nom_utilisateur VARCHAR(20) NOT NULL, 
	prenom_utilisateur VARCHAR(20),
	login_utilisateur VARCHAR(20) NOT NULL, 
	password_utilisateur VARCHAR(20) NOT NULL, 
	id_typeutil SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	PRIMARY KEY (_id_utilisateur_),
	FOREIGN KEY (id_typeutil) REFERENCES TYPE_UTILISATEUR(id_typeutil)
	
	
);


create table SONDE (
	_id_sonde_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	nom_sonde VARCHAR(20) NOT NULL, 
	prenom_sonde VARCHAR(20) NOT NULL, 
	sexe_sonde VARCHAR(20) NOT NULL, 
	datenaiss_sonde DATE, 
	tel_sonde VARCHAR(14)
	PRIMARY KEY (_id_sonde_)
);

create table QUESTIONNAIRE (
	_id_questionnaire_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_questionnaire VARCHAR(100), 
	dateheurelim_questionnaire DATE, 
	accessible_questionnaire BOOLEAN, 
	termine_questionnaire BOOLEAN, 
	analyse_questionnaire BOOLEAN,
	#aaaa-mm-jj_hh:mm:ss:ms, 
	url_analyse VARCHAR(100),  
	id_utilisateur SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	id_panel SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	id_entreprise SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
	FOREIGN KEY (id_panel) REFERENCES PANEL(id_panel),
	FOREIGN KEY (id_entreprise) REFERENCES ENREPRISE(id_entreprise),
	PRIMARY KEY (_id_questionnaire_)
);

create table SONDER (
	_id_utilisateur_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	_id_sonde_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	_id_questionnaire_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	 dateheure_sondage DATE,
	PRIMARY KEY (_id_utilisateur_),
	PRIMARY KEY (_id_sonde_),
	PRIMARY KEY (_id_questionnaire_),
	FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
	FOREIGN KEY (_id_sonde_) REFERENCES SONDE(_id_sonde_),
	FOREIGN KEY (id_entreprise) REFERENCES ENREPRISE(id_entreprise)

);

create table VILLE (
	_codeinsee_ville_ VARCHAR(5) NOT NULL, 
	nom_ville VARCHAR(50), 
	codepostal_ville VARCHAR(5),
	PRIMARY KEY(_codeinsee_ville_)
);

create table CSP (
	_id_csp_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_csp VARCHAR(100),
	PRIMARY KEY(_id_csp_)
);


create table APPARTENIR (
	_id_panel_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	_id_sonde SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (_id_panel_),
	PRIMARY KEY (_id_sonde),
	FOREIGN KEY (_id_panel_) REFERENCES PANEL(_id_panel_),
	FOREIGN KEY (_id_sonde_) REFERENCES SONDE(_id_sonde_),
);

create table ADRESSE (
	_id_adresse_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	numero_adresse INTEGER(10), 
	bister_adresse VARCHAR(3), 
	libellevoie_adresse VARCHAR(150), 
	batiment_adresse VARCHAR(5), 
	etage_adresse VARCHAR(3), 
	escalier_adresse VARCHAR(2), 
	appartement_adresse VARCHAR(10), 
	codeinsee_ville VARCHAR(5) NOT NULL,
	PRIMARY KEY (_id_adresse_),
	FOREIGN KEY (codeinsee_ville) REFERENCES VILLE(codeinsee_ville)

);

create table CHOIX_MULTIPLE (
	_id_choixmul_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_choixmul VARCHAR(100), 
	id_question SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT
	PRIMARY KEY (_id_choixmul_),
	FOREIGN KEY (id_question) REFERENCES QUESTION(id_question)
);

create table PANEL (
	_id_panel_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	intitule_panel VARCHAR(100),
	PRIMARY KEY (intitule_panel)
);

create table QUESTION (
	_id_question_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	enonce_question VARCHAR(100), 
	urlanal_question VARCHAR(100), 
	#id_typequest SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	#id_questionnaire SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (_id_question_),
	FOREIGN KEY (id_typequest) REFERENCES TYPE_QUESTION(id_typequest),
	FOREIGN KEY (id_questionnaire) REFERENCES QUESTIONNAIRE(id_questionnaire)
);



create table ENTREPRISE (
	_id_entreprise_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	nom_entreprise VARCHAR(100), 
	tel_entreprise VARCHAR(14), 
	email_entreprise VARCHAR(133), 
	id_adresse SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (_id_entreprise_),
	FOREIGN KEY (id_adresse) REFERENCES ADRESSE(id_adresse)
);

create table TYPE_QUESTION (
	_id_typequest_ SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	libelle_typequest VARCHAR(10),
	PRIMARY KEY (_id_typequest_)
);

create table ENREGISTRER_NOTE (
	_#id_question_, 
	_#aaaa-mm-jj_hh:mm:ss:ms_, 
	note
)

create table ENREGISTRER_REPONSE (
	_#id_question_, 
	_#aaaa-mm-jj_hh:mm:ss:ms_, 
	commentaire
)


create table ENREGISTRER_CHOIX (
	_#id_question_, 
	_#aaaa-mm-jj_hh:mm:ss:ms_,
	_#id_choixmul_
)


create table ENREGISTRER_CLASSEMENT (
	_#id_question_,
	 _#aaaa-mm-jj_hh:mm:ss:ms_, 
	_#id_choixmul_, 
	position
);






ENREGISTRER_SELECTION (_#id_question_, _#aaaa-mm-jj_hh:mm:ss'ms_, _#id_choixmul₎





