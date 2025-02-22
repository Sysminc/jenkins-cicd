import unittest
import requests
from flask import Flask

# Unit test untuk cek website eksternal
class TestWebsite(unittest.TestCase):
    def test_website_is_up(self):
        url = "http://192.168.10.147:5000"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

# Contoh aplikasi Flask untuk diuji
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!", 200

# Unit test untuk cek endpoint Flask
class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_home_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, Flask!")

if __name__ == "__main__":
    unittest.main()


