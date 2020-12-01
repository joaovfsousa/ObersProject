import os
from datetime import datetime

from flask import Flask, request

from utils.cpf_validator import cpf_validator

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
  response = {
    "status": 200,
    "message": "All right with the service",
    "code": "success",
    "data": {
      "environment": os.environ.get("FLASK_ENV"),
      "datetime_server": datetime.now().isoformat(),
      "version": "1-0-2"
    }
  }
  return response


@app.route('/validator/Cpf', methods=['POST'])
def validador_cpf():
  cpf = request.get_json()["cpf"]

  is_cpf_valid = cpf_validator(cpf)

  code = "success" if is_cpf_valid else "error"
  cpf_status = "cpf is valid" if is_cpf_valid else "cpf is not valid"

  response = {
    "status": 200,
    "cpf": str(cpf),
    "code": code,
    "data": cpf_status
  }

  return response


if __name__ == '__main__':
  app.run(port=9095)
