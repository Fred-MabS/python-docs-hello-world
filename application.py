from flask import Flask, jsonify, make_response
app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def hello(name=None):
    if not name:
        message = jsonify(message='missing parameter')
        return make_response(message, 400)
    data = {'message': f'Hello {name}!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
