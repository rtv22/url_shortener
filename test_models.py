from models import Link
from extensions import db
from main import create_app


class TestModels:

    def setup(self):
        with create_app().app_context():

            db.create_all()

            db.session.query(Link).delete()

            original_urls = ['https://google.com',
                             'https://www.avito.ru/',
                             'https://hh.ru/',
                             'https://bulma.io/']

            for url in original_urls:
                db.session.add(Link(original_url=url))

            db.session.commit()

    def test_generate_short_link(self):
        with create_app().app_context():
            assert db.session.query(Link).count() == 4
