

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
    def test_register_route_status(self, client):
        """Tests register route status."""
        res = client.get('/register')
        assert res.status_code == 200

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

    def test_registration_redirect_status(self, client):
        """Test user is redirected to login page after registration."""
        res = client.post(
            '/register',
            data={'email': 'test@test.com', 'password': 'password'},
            follow_redirects=True
        )
        assert b'Stock - Login' in res.data

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

    def test_login_to_portfolio_redirect(self, client, user, company):
        """Test that the user is redirected to their portfolio page"""
        res = client.post(
            '/login',
            data={'email': 'test@test.com', 'password': 'password'},
            follow_redirects=True
        )
        expected = f'{company.name}'
        assert expected.encode() in res.data

    def test_logout_redirect_status(self, authenticated_client):
        """Tests that a signed in user can log out."""
        res = authenticated_client.get(
            '/logout',
            follow_redirects=True
        )

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
    