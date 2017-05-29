from flask import url_for

from app import db

class Sondage(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return "<Sondage (%d) %s>" % (self.id, self.name)


class Question(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(120))
    sondage_id = db.Column(db.Integer, db.ForeignKey('sondage.id'))
    sondage = db.relationship("Sondage", backref=db.backref("questions", lazy="dynamic", cascade="all, delete-orphan"))

    def __repr__(self):
        return "<Question (%d) %s>" % (self.id, self.title)


class SimpleQuestion(Question):

    __table_args__={ "extend_existing" : True}

    firstAlternative = db.Column(db.String(120))
    secondAlternative = db.Column(db.String(120))

    firstChecked = db.Column(db.Boolean)



class User(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return "<User (%d) %s>" % (self.id, self.name)

