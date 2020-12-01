import flask

app = flask.Flask(__name__)

app.debug = True


@app.route('/health', methods=['GET'])
def health():
  response = {
    "status": 200,
    "message": "All right with the service",
    "code": "success",
    "data": {
      "environment": "development",
      "datetime_server": "2020-11-03T14:34:58.139738",
      "version": "1-0-2"
    }
  }
  return response


if __name__ == '__main__':
  app.run(port=9095)
