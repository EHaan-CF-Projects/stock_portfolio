from src.models import Company, db


def test_create_company(session):
    company = Company(name='Google', symbol='GOOG')
    session.add(company)
    session.commit()

    assert company.id > 0

    companies = Company.query.all()

    assert companies[0].name == 'Google'

