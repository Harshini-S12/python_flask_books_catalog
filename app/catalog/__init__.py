# app/catalog/__init__.py
from flask import Blueprint

from app import db
from app.catalog.models import Book, Publication

main = Blueprint('main', __name__, template_folder='templates')

from app.catalog import routes

p1 = Publication("Oxford Publications")
p2 = Publication("Paramount Press")
p3 = Publication("Oracle Books Inc")
p4 = Publication("Vintage Books and Comics")
p5 = Publication("Trolls Press")
p6 = Publication("Broadway Press")
p7 = Publication("Downhill Publishers")
p8 = Publication("Kingfisher Inc")
db.session.add_all([p2, p3, p4, p5, p6, p7, p8])
db.session.commit()



