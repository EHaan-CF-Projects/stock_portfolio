from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CompanyForm(FlaskForm):
    """
    """
    zipcode = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    zipcode = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
