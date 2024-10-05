import unittest
from utils.authentication import generate_qr_code

class TestQRCodeGeneration(unittest.TestCase):
    def test_qr_code_creation(self):
        email = "test@example.com"
        qr_code_path = generate_qr_code(email)
        self.assertTrue(os.path.exists(qr_code_path))

if __name__ == "__main__":
    unittest.main()