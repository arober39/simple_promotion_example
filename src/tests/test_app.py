# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertIn('status', response.json)

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()
