import unittest
from app import create_app
from app.utils.database import db
from app.models.user import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_and_login(self):
        with self.app.test_client() as client:
            response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
            self.assertEqual(response.status_code, 201)

            response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()