import os
from datetime import datetime

from flask import Flask, request

from utils.cpf_validator import cpf_validator
from utils.cnpj_validator import cnpj_validator

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


@app.route('/validator/Cnpj', methods=['POST'])
def validador_cnpj():
  cnpj = request.get_json()["cnpj"]

  is_cnpj_valid = cnpj_validator(cnpj)

  code = "success" if is_cnpj_valid else "error"
  cnpj_status = "cnpj is valid" if is_cnpj_valid else "cnpj is not valid"

  response = {
    "status": 200,
    "cnpj": str(cnpj),
    "code": code,
    "data": cnpj_status
  }

  return response


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=9095)
