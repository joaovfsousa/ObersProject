import unittest
import json

from app import app


class ValidatorCpfRouteTest(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()

  def test_post_valid_cpf(self):
    payload = json.dumps({
      "cpf": 15493825007
    })

    expected = {
      "status": 200,
      "cpf": "15493825007",
      "code": "success",
      "data": "cpf is valid"
    }

    response = self.app.post(
      '/validator/Cpf',
      headers={"Content-Type": "application/json"},
      data=payload
    )

    self.assertEqual(response.json, expected)

  def test_post_invalid_cpf(self):
    payload = json.dumps({
      "cpf": 15493825006
    })

    expected = {
      "status": 200,
      "cpf": "15493825006",
      "code": "error",
      "data": "cpf is not valid"
    }

    response = self.app.post(
      '/validator/Cpf',
      headers={"Content-Type": "application/json"},
      data=payload
    )

    print("AAA", response.json, "AAA")

    self.assertEqual(response.json, expected)
