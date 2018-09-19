import unittest
import json
from app import app

class TestRequest(unittest.TestCase):
   def test_post(self):
      app2 = app.test_client()
 
      response = app2.post('/v1/products',data=json.dumps({"id": "123", "name": "teste"}))
      self.assertEqual(200, response.status_code)
      response = app2.post('/v1/products',data=json.dumps({"id": "123", "name": "teste"}))
      self.assertEqual(403, response.status_code)

if __name__ == '__main__':
   unittest.main()
