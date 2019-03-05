from flask import render_template, request, redirect, url_for, abort
from sqlalchemy.exc import DBAPIError, IntegrityError
import requests
import json
from . import app
from .models import Company, db


@app.route('/')
def home():
    """Function to render the home page.
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search_form():
    """Function that will render the search page.
    """
    form = CityForm()

    if form.validate_on_submit():
        symbol = form.data['symbol']

        url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)
        response = requests.get(url)
        data = json.loads(response.text)
        session['context'] = data
        session['symbol'] = symbol

        return redirect(url_for('.preview_company'))

    return render_template('./stocks/search.html', form=form), 200


@app.route('/company', methods=['GET', 'POST'])
def preview_company():
    """
    """
    form_context = {
        'name': session['context']['name'],
        'symbol': session['symbol']
    }
    form = CityAddForm(**form_context)

    if form.validate_on_submit():
        try:
            company = Company(name=form.data['name'], symbol=form.data['symbol'])
            db.session.add(city)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            # insert flash?
            return render_template('./stocks/search.html', form=form)

        return redirect(url_for('.portfolio'))


@app.route('/portfolio')
def portfolio():
    """Function that will render the portfolio page.
    """
    return render_template('./stocks/stocks.html'), 200
