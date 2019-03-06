from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(256), index=True, unique=True)
    symbol = db.Column(db.String(256), index=True, unique=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Company {}-{}>'.format(self.name, self.symbol)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)

    companies = db.relationship('Company', backref='category', lazy=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Category {}>'.format(self.name)
