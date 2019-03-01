from flask import render_template, request, redirect, url_for
import requests
import json  # to parse incoming data from api
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
    return render_template('./stocks/search.html')


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
    company = Company(name=data['companyName'], symbol=data['symbol']) #'name' needs to match the database column, 'companyName' needs to match what is returned from the JSON

    # store results in database
    db.session.add(company)
    db.session.commit()  # adds infor to the database here
    return company.name

    # redirect to porfolio page
    # return redirect(url_for('.portfolio'))  # .portfolio for the portfolio function, then it finds and references the decorator's route.


@app.route('/portfolio')
def portfolio():
    """Function that will render the portfolio page.
    """
    return render_template('./stocks/stocks.html')
#     return str(Company.query.all())
