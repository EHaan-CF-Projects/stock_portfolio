from flask import render_template, request, redirect, url_for, abort, session
from sqlalchemy.exc import DBAPIError, IntegrityError
import requests
import json
from . import app
from .models import Company, db
from .forms import CompanyForm, CompanyAddForm


@app.route('/')
def home():
    """Function to render the home page.
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search_form():
    """Function that will render the search page.
    """
    form = CompanyForm()

    if form.validate_on_submit():
        symbol = form.data['symbol']

        url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(symbol)

        response = requests.get(url)
        data = json.loads(response.text)
        session['name'] = data['companyName']
        session['symbol'] = data['symbol']

        return redirect(url_for('.preview_company'))

    return render_template('./stocks/search.html', form=form), 200


@app.route('/company', methods=['GET', 'POST'])
def preview_company():
    """
    """
    form_context = {
        'name': session['name'],
        'symbol': session['symbol'],
    }
    form = CompanyAddForm(**form_context)

    if form.validate_on_submit():
        try:
            company = Company(name=form.data['name'], symbol=form.data['symbol'])
            db.session.add(company)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            # insert flash?
            return render_template('./stocks/search.html', form=form)

        return redirect(url_for('.portfolio'))

    return render_template(
        './stocks/company.html',
        form=form,
        symbol=form_context['symbol'],
        name=session['name'],
        ), 200


@app.route('/portfolio')
def portfolio():
    """Function that will render the portfolio page.
    """
    return render_template('./stocks/stocks.html'), 200
