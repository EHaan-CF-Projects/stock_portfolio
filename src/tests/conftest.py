from src.models import Company, Portfolio, User
from src.models import db as _db
from src import app as _app
import pytest
import os

# ====General Test Setup =====


@pytest.fixture()
def app(request):
    """Testable flask application"""
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        """Cleans up and closes out test session."""
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


# ==== Test Database Setup =====


@pytest.fixture()
def session(db, request):
    """New test session for database."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session  # DO NOT SKIP THIS LINE!!!!!!

    def teardown():
        """Clears and removes test database."""
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def db(app, request):
    """Testable application databases."""
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture()
def portfolio(session):
    """Testable portfolio databse table."""
    portfolio = Portfolio(name='Default')

    session.add(portfolio)
    session.commit()

    return portfolio


@pytest.fixture()
def company(session, portfolio):
    """Testable Company database table."""
    company = Company(name='Google', symbol='goog', portfolio=portfolio)

    session.add(company)
    session.commit()

    return company


@pytest.fixture()
def user(session):
    """Testable User database table."""
    user = User(email='test@test.com', password='password')

    session.add(user)
    session.commit()
    return user

# ==== Test Client Setup =====


@pytest.fixture()
def client(app, db, session):
    """Testable client requests."""
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture()
def authenticated_client(client, user):
    """Testable authenticated client"""
    client.post(
        '/login',
        data={'email': user.email, 'password': 'password'},
        follow_redirects=True,
    )
    return client
