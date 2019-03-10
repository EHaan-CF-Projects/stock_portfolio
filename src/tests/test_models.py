# from src.models import Company, Portfolio


# class TestCompanyModel:
#     """Test new company item."""
#     def test_create_company(self, company):
#         """New company row is added to Company table."""
#         assert company.id > 0

#     def test_company_name(self, company):
#         """New company name added successfully."""
#         assert company.name == 'Google'

#     def test_company_symbol(self, company):
#         """New company symbol symbol added successfully"""
#         assert company.symbol == 'goog'

#     def test_company_portfolio_id(self, company):
#         """New company has associated portfolio"""
#         assert company.portfolio_id > 0


# class TestPortfolioModel:
#     """Test new portfolio item."""
#     def test_create_portfolio(self, portfolio):
#         assert portfolio.id > 0

#     def test_portfolio_name(self, portfolio):
#         assert portfolio.name == 'Default'

# #  TEST NOT WORKING - USER ID PULLED FROM SESSION INTO PORTFOLIO DATABASE?
#     # def test_portfolio_user_id(self, portfolio):
#     #     assert portfolio.user_id == 1


# class TestUserModel:
#     """Test new user records."""
#     def test_user_create(self, user):
#         """Test that a new user is added to the database on registration"""
#         assert user.id > 0

#     def test_user_email(self, user):
#         """Test that a user's email is added."""
#         assert user.email == 'test@test.com'

#     def test_user_check_password(self, user):
#         """Test that a user's password is added."""
#         from src.models import User
#         assert User.check_password_hash(user, 'password')
