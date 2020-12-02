import unittest
import json

from app import app


class ValidatorCnpjRouteTest(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()

  def test_post_valid_cnpj(self):
    payload = json.dumps({
      "cnpj": "04182131000198"
    })

    expected = {
      "status": 200,
      "cnpj": "04182131000198",
      "code": "success",
      "data": "cnpj is valid"
    }

    response = self.app.post(
      '/validator/Cnpj',
      headers={"Content-Type": "application/json"},
      data=payload
    )

    self.assertEqual(response.json, expected)

  def test_post_invalid_cnpj(self):
    payload = json.dumps({
      "cnpj": "12345678901234"
    })

    expected = {
      "status": 200,
      "cnpj": "12345678901234",
      "code": "error",
      "data": "cnpj is not valid"
    }

    response = self.app.post(
      '/validator/Cnpj',
      headers={"Content-Type": "application/json"},
      data=payload
    )

    self.assertEqual(response.json, expected)
