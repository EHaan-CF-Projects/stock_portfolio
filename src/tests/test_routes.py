class TestBaseRoutes:
    """
    """
    def test_home_route_status(self, client):
        """
        """
        res.client.get('/')
        assert res.status_code == 200

    
    