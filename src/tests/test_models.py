from src.models import Company, Portfolio


class TestCompanyModel:
    """
    """
    def test_create_company(self, company):
        """
        """
        assert company.id > 0


class TestPortfolioModel:
    """
    """
    def test_create_portfolio(self, portfolio):
        assert portfolio.id > 0

    def test_portfolio_name(self, portfolio):
        assert portfolio.name is not None


class TestPortfolioCompanyRelationship:
    """
    """
    def test_company_has_portfolio(self):
        hybrid = Portfolio(name='hybrid')
        google = Company(name='Google', symbol='goog', portfolio=hybrid)

        assert google.portfolio.name == 'hybrid'

    def test_company_has_cities(self):
        hybrid = Portfolio(name='hybrid')
        google = Company(name='Google', symbol='goog', portfolio=hybrid)
        apple = Company(name='Apple', symbol='aapl', portfolio=hybrid)

        assert google.portfolio.name == 'hybrid'
        assert google.portfolio.name == 'hybrid'
