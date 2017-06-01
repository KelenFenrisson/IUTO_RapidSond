from .application import db

class RoleUtilisateur(db.Model):
    __tablename__="roleutilisateur"
    id=db.Column(db.String(1), primary_key=True)
    intitule=db.Column(db.String(30))

class Utilisateur(db.Model):
    __tablename__="utilisateur"
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(30))
    prenom=db.Column(db.String(30))
    login=db.Column(db.String(30))
    password=db.Column(db.String(30))
    role_id=db.Column(db.String(1), db.ForeignKey(RoleUtilisateur.id))

class Client(db.Model):
    __tablename__="client"
    id=db.Column(db.Integer, primary_key=True)
    raison=db.Column(db.String(30))
    adresse=db.Column(db.String(30))
    compl_adresse=db.Column(db.String(30))
    code_postal=db.Column(db.Integer)
    ville=db.Column(db.String(30))
    tel=db.Column(db.String(20))
    email=db.Column(db.String(130))

class Panel(db.Model):
    __tablename__="panel"
    id=db.Column(db.Integer, primary_key=True)
    intitule=db.Column(db.String(30))

class Categorie(db.Model):
    __tablename__="categorie"
    id=db.Column(db.String(1), primary_key=True)
    intitule=db.Column(db.String(50))

class Tranche(db.Model):
    __tablename__="tranche"
    id=db.Column(db.String(1), primary_key=True)
    valdebut=db.Column(db.Integer)
    valfin=db.Column(db.Integer)

class Caracteristique(db.Model):
    __tablename__="caracteristique"
    id=db.Column(db.String(3), primary_key=True)
    sexe=db.Column(db.String(1))
    tranche_id=db.Column(db.String(1), db.ForeignKey(Tranche.id))
    categorie=db.Column(db.String(1), db.ForeignKey(Categorie.id))


class Questionnaire(db.Model):
    __tablename__="questionnaire"
    id=db.Column(db.Integer, primary_key=True)
    titre=db.Column(db.String(30))
    etat=db.Column(db.String(1))
    client_id= db.Column(db.Integer, db.ForeignKey(Client.id))
    concepteur_id= db.Column(db.Integer, db.ForeignKey(Client.id))
    panel_id= db.Column(db.Integer, db.ForeignKey(Panel.id))

class TypeQuestion(db.Model):
    __tablename__="typequestion"
    id=db.Column(db.String(1), primary_key=True)
    intitule=db.Column(db.String(30))
    type_reponse=db.Column(db.String(10))

class Question(db.Model):
    __tablename__="question"
    id=db.Column(db.Integer, primary_key=True)
    numero= db.Column(db.Integer, primary_key=True)
    intitule=db.Column(db.String(2000))
    max_val=db.Column(db.Integer)
    type_id=db.Column(db.String(1), db.ForeignKey(TypeQuestion.id))

class ValeurPossible(db.Model):
    __tablename__="valeurpossible"
    question_id = db.Column(db.Integer, db.ForeignKey(Question.id),primary_key=True)
    question_num = db.Column(db.Integer, db.ForeignKey(Question.numero),primary_key=True)
    id=db.Column(db.Integer, primary_key=True)
    valeur=db.Column(db.Text)

class Sonde(db.Model):
    __tablename__="sonde"
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(30))
    prenom=db.Column(db.String(30))
    date_naissance=db.Column(db.String(10))
    telephone=db.Column(db.String(10))
    caracteristique_id=db.Column(db.String(1), db.ForeignKey(Caracteristique.id))

class Constituer(db.Model):
    __tablename__="constituer"
    sonde_id=db.Column(db.Integer, db.ForeignKey(Sonde.id), primary_key=True)
    panel_id=db.Column(db.Integer, db.ForeignKey(Panel.id), primary_key=True)

class Interroger(db.Model):
    __tablename__="interroger"
    utilisateur_id=db.Column(db.Integer, db.ForeignKey(Utilisateur.id), primary_key=True)
    sonde_id=db.Column(db.Integer, db.ForeignKey(Sonde.id), primary_key=True)
    questionnaire_id=db.Column(db.Integer, db.ForeignKey(Questionnaire.id), primary_key=True)

class Repondre(db.Model):
    __tablename__="repondre"
    questionnaire_id=db.Column(db.Integer, db.ForeignKey(Questionnaire.id), primary_key=True)
    numero_question=db.Column(db.Integer, db.ForeignKey(Question.numero), primary_key=True)
    caracteristique_id=db.Column(db.String(1), db.ForeignKey(Caracteristique.id), primary_key=True)
    valeur=db.Column(db.String(30), primary_key=True)