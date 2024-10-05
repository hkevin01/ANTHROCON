import unittest
from utils.authentication import register_user, login_user

class TestAuthentication(unittest.TestCase):
    def test_register_and_login(self):
        email = "test@example.com"
        password = "securepassword"
        
        register_user(email, password)
        user_data = login_user(email, password)
        self.assertIsNotNone(user_data)

if __name__ == "__main__":
    unittest.main()