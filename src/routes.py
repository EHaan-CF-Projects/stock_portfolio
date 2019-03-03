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


@app.route('/search', methods=['GET'])
def search_form():
    """Function that will render the search page.
    """
    return render_template('./stocks/search.html'), 200


@app.route('/search', methods=['POST'])
def search_results():
    """
    """
    # hit API with given stock symbol
    symbol = request.form.get('symbol')
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)
    response = requests.get(url)

    # # normalize data
    data = json.loads(response.text)
    try:
        company = Company(name=data['companyName'], symbol=data['symbol'])

        # store results in database
        db.session.add(company)
        db.session.commit()  # adds infor to the database here
    except (DBAPIError, IntegrityError):
        abort(400)
    # redirect to porfolio page
    return redirect(url_for('.portfolio')), 302  # .portfolio for the portfolio function, then it finds and references the decorator's route.


@app.route('/portfolio')
def portfolio():
    """Function that will render the portfolio page.
    """
    return render_template('./stocks/stocks.html'), 200


