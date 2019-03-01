from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    symbol = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Company {}-{}>'.format(self.name, self.symbol)
