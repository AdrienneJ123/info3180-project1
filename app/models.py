from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120))
    description = db.Column(db.Text)

    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)

    location = db.Column(db.String(120))
    price = db.Column(db.String(120))

    property_type = db.Column(db.String(50))

    photo = db.Column(db.String(120))
