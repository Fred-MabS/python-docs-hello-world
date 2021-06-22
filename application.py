from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route("/<string:name>", methods=["GET"])
def hello(name=None):
    """Gist detail view.
    ---
    get:
      parameters:
      - in: path
        schema: NameParameter
      responses:
        200:
          description: OK
    """
    if not name:
        message = jsonify(message='missing parameter')
        return make_response(message, 400)
    data = {'message': f'Hello {name}!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
