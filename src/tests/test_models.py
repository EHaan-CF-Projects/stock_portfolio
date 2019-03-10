from src.models import Company, Portfolio


class TestCompanyModel:
    """Test new company item."""
    def test_create_company(self, company):
        """New company row is added to Company table."""
        assert company.id > 0

    def test_company_name(self, company):
        """New company name added successfully."""
        assert company.name == 'Google'

    def test_company_symbol(self, company):
        """New company symbol symbol added successfully"""
        assert company.symbol == 'goog'

    def test_company_portfolio_id(self, company):
        """New company has associated portfolio"""
        assert company.portfolio_id > 0


class TestPortfolioModel:
    """Test new portfolio item."""
    def test_create_portfolio(self, portfolio):
        assert portfolio.id > 0

    def test_portfolio_name(self, portfolio):
        assert portfolio.name == 'Default'

#  TEST NOT WORKING - USER ID PULLED FROM SESSION INTO PORTFOLIO DATABASE?
    # def test_portfolio_user_id(self, portfolio):
    #     assert portfolio.user_id == 1
