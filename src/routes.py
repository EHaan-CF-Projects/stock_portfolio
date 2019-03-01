from flask import render_template, request, redirect, url_for
import json #to parse incoming data from api
from . import app
# from .models import Company, db


@app.route('/')
def home():
    """
    """
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def search_form():
    """
    """
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search_results():
    """
    """
    # hit API with given stock symbol
    symbol = request.form.get('symbol')  # request imported from flask
    url = f'https://api.iextrading.com/1.0/stock/{symbol}/company'
    response = requests.get(url)

    # normalize data
    data = json.loads(response.text)
    company = Company(name=data['companyName'], symbol=data['symbol']) #'name' needs to match the database column, 'companyName' needs to match what is returned from the JSON

    # # store results in database
    # db.session.add(company)
    # db.session.commit()  # adds infor to the database here


    # # redirect to porfolio page
    # return redirect(url_for('.portfolio'))  # .portfolio for the portfolio function, then it finds and references the decorator's route.


@app.route('/portfolio')
def portfolio():
    """
    """
    return str(Company.query.all())
