

class TestBaseRoutes:
    """Test base routes."""
    def test_home_route_status(self, client):
        """Test home route status code."""
        res = client.get('/')
        assert res.status_code == 200

    def test_home_route_body(self, client):
        """Test home route content."""
        res = client.get('/')
        assert b'Stock - Home' in res.data

    def test_unknown_route_status(self, client):
        """Tests 404 error for unknown routes."""
        res = client.get('/not_here')
        assert res.status_code == 404


class TestAuthentication:
    """Tests for user authentication and access."""

    # Nav Bar

    def test_has_correct_nav_when_not_logged_in(self, client):
        res = client.get('/')
        assert b'<a href="/"' in res.data
        assert b'<a href="/register"' in res.data
        assert b'<a href="/login"' in res.data
        assert b'<a href="/logout"' not in res.data

    def test_has_correct_nav_when_logged_in(self, authenticated_client):
        res = authenticated_client.get('/')
        assert b'<a href="/"' in res.data
        assert b'<a href="/register"' not in res.data
        assert b'<a href="/login"' not in res.data
        assert b'<a href="/logout"' in res.data

    def test_register_route_status(self, client):
        """Tests register route status."""
        res = client.get('/register')
        assert res.status_code == 200

    # Register
    def test_registration_body(self, client):
        """Tests register route content."""
        res = client.get('/register')
        assert b'Stock - Register' in res.data

    def test_register_invalid_inputs(self, client):
        """Test that user is redirected back to register page if inputs are invalid."""
        res = client.post(
            '/register',
            follow_redirects=True
        )
        assert b'Stock - Register' in res.data

    def test_user_already_exists(self, client):
        credentials = {'email': 'test@test.com', 'password': 'password'}
        res = client.post('/register', data=credentials, follow_redirects=True)
        res = client.post('/register', data=credentials, follow_redirects=True)
        assert b'test@test.com has already been registered.' in res.data
        assert b'<title>Stock - Register</title>' in res.data

    def test_registration_redirect_status(self, client):
        """Test user is redirected to login page after registration."""
        res = client.post(
            '/register',
            data={'email': 'test@test.com', 'password': 'password'},
            follow_redirects=True
        )
        assert b'Stock - Login' in res.data

# Login
    def test_login_page_status(self, client):
        """Test register route status"""
        res = client.get('/login')
        assert res.status_code == 200

    def test_login_page_content(self, client):
        res = client.get('/login')
        assert b'Stock - Login'

    def test_registered_user_can_login(self, client):
        """Test that the user is able to login after being a registered user."""
        res = client.post(
            '/register',
            data={'email': 'test@test.com', 'password': 'password'},
            follow_redirects=True
        )
        res = client.post(
            '/login',
            data={'email': 'test@test.com', 'password': 'password'},
            follow_redirects=True
        )
        assert res.status_code == 200
        assert b'Stock - Stocks' in res.data

    def test_login_invalid_inputs(self, client):
        """Test that a user is redirected back to login page if inputs are invalid"""
        res = client.post(
            '/login',
            follow_redirects=True
        )
        assert b'Stock - Login' in res.data

    # def test_login_to_portfolio_redirect(self, client, user, company):
    #     """Test that the user is redirected to their portfolio page"""
    #     res = client.post(
    #         '/login',
    #         data={'email': 'test@test.com', 'password': 'password'},
    #         follow_redirects=True
    #     )
    #     expected = f'{company.name}'
    #     assert expected.encode() in res.data

    # Logout

    def test_logout_redirect_status(self, authenticated_client):
        """Tests that a signed in user can log out."""
        res = authenticated_client.get(
            '/logout',
            follow_redirects=True
        )
        assert res.status_code == 200

    def test_logout_unauthenticated(self, client):
        """Tests an unauthenticated logout status."""
        res = client.get('/logout')
        assert res.status_code == 404


class TestAuthenticatedRoutes:
    """Test protected routes."""
    def test_search_route_status(self, authenticated_client):
        """Tests search route status."""
        res = authenticated_client.get('/search')
        assert res.status_code == 200

    def test_search_route_content(self, authenticated_client):
        """Tests search route content."""
        res = authenticated_client.get('/search')
        assert b'Stock - Search' in res.data

    def test_search_route_status_unauthenticated(self, client):
        """Tests that a user who is not signed in will be prevented."""
        res = client.get('/search')
        assert res.status_code == 404
    
    def test_search_to_preview_redirect_status(self, authenticated_client, company):
        """Test search to preview pages redirect status."""
        res = authenticated_client.post(
            '/search',
            data={'symbol': 'goog'},
            follow_redirects=True
        )
        assert res.status_code == 200

    def test_search_to_company_preview_content(self, authenticated_client):
        """Test user is redirected to preview page."""
        res = authenticated_client.post(
            '/search',
            data={'symbol': 'goog'},
            follow_redirects=True
        )
        assert b'Stock - Preview' in res.data

    def test_company_preview_route_status_unauthenticated(self, client):
        """Test unauthenticated user cannot preview company."""
        res = client.get('/company')
        assert res.status_code == 404

    def test_preview_to_portfolio_redirect_status(self, authenticated_client, company):
        """Tests a user will be redirected to portfolios page."""
        res = authenticated_client.post(
            '/search',
            data={'symbol': 'goog'},
            follow_redirects=True
        )
        res = authenticated_client.post(
            '/company',
            data={'name': 'Google', 'symbol': 'goog', 'portfolio_id': 1},
            follow_redirects=True
        )
        assert res.status_code == 200

    def test_portfolio_route_status_code(self, authenticated_client, company, portfolio):
        """Test portfolio route status."""
        res = authenticated_client.get('/portfolio')
        assert res.status_code == 200

    def test_portfolio_route_content(self, authenticated_client, company, portfolio):
        res = authenticated_client.get('/portfolio')
        assert b'Stock - Stocks' in res.data

    def test_portfolio_route_status_unauthenticated(status, client, company, portfolio):
        res = client.get('/portfolio')
        assert res.status_code == 404

    def test_portfolio_to_search_redirect_status(self, authenticated_client, company, portfolio, user):
        res = authenticated_client.post(
            '/portfolio',
            data={'name': 'Test', 'user_id': 1},
            follow_redirects=True
        )
        assert res.status_code == 200

## Missing tests: portfolio selection dropdown, portfolio list