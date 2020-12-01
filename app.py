import flask

app = flask.Flask(__name__)

app.debug = True


@app.route('/', methods=['GET'])
def root():
  return dict(message='Success')


app.run(port=9095)
