import unittest

from app import app


class HealthRouteTest(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()

  def test_health_route_response(self):
    response = self.app.get('/health')
    expected = {
      "status": 200,
      "message": "All right with the service",
      "code": "success",
      "data": {
        "environment": "development",
        "datetime_server": "2020-11-03T14:34:58.139738",
        "version": "1-0-2"
      }
    }

    self.assertEqual(response.json["status"], expected["status"])
    self.assertEqual(response.json["message"], expected["message"])
    self.assertEqual(response.json["code"], expected["code"])
    self.assertEqual(
      response.json["data"]["environment"],
      expected["data"]["environment"]
    )

  def test_health_route_status_code(self):
    response = self.app.get('/health')
    expected = 200
    self.assertEqual(response.status_code, expected)


if __name__ == "__main__":
  unittest.main()
