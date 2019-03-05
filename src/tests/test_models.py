from src.models import Company, db


def test_create_company(session):
    company = Company(name='Google', symbol='GOOG')
    session.add(company)
    session.commit()

    assert company.id > 0

    # companies = Company.query.all()

    # assert companies == 1


# def test_create_another_company(session):
#     company = Company(name='Apple', symbol='aapl')
#     session.add(company)
#     session.commit()

#     assert company.id > 0
