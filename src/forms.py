from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CompanyForm(FlaskForm):
    """
    """
    symbol = StringField('Company Symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
