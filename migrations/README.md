# Stock Portfolio

**Author**: Evy Haan
**Version**: 1.0.0

## Overview
With this site, users can search and store companies in the stock exchange for future reference.

## Getting Started
To build this app, a developer will want to setup a virtual environment (see Architechture for libraries & modules), a .env file that includes a route to the wsgi.py file, flask-env status, and database url (and api key if used), as well as set up a database to hold incoming API information. Static files will be referenced using Flask, and templates can be pre-built and ready in appropriate static directories.

## Architechture
Languages: Python, HTML5, CSS3, Postgres
Virtual Environment: Pipenv
Packages(modules): Python-dotenv, flask(render_template,request, redirect, abort, url_for), flask-sqlalchemy(SQLAlchemy,DBAPIError, IntegrityError), flask-migrate (Migrate), requests, psychopg2-binary
Python Modules: json, os



## API
The IEX API was used for this app. It is free, and while use options include the need for an API key, it is not required for all requests. An API key was not used in this app. Docs for using the EIX API can be found here: https://iextrading.com/developer/docs/#getting-started
