from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from .models import Portfolio, Company, db
from flask import g


class CompanyForm(FlaskForm):
    """
    """
    symbol = StringField('Company Symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    portfolios = SelectField('portfolio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(c.id), c.name) for c in Portfolio.query.all()]


class PortfolioCreateForm(FlaskForm):
    """
    """
    name = StringField('portfolio', validators=[DataRequired()])


class AuthForm(FlaskForm):
    """
    """
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
