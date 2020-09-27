from flask import request

from main import create_app


class TestRoutes:
    def setup(self):
        create_app().testing = True
        self.client = create_app().test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_add_link_404(self):
        response = self.client.get('/add_link')
        assert response.status_code == 404

    def test_stats(self):
        response = self.client.get('/stats')
        assert response.status_code == 200

    def teardown(self):
        pass
