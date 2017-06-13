from .application import manager, db, mkpath
from .models import *

@manager.command
def syncdb():
    db.create_all()