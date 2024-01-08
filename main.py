from turbo import FlaskAPI, request, abort, jsonify, validate_token

app = FlaskAPI(__name__)

# Home URL
## Extra path will show the same screen for any url past the /
@app.add_endpoint('/', methods=['GET'])
@app.add_endpoint('/<path:extra>', methods=['GET'])
def home(extra=None):
    return jsonify({'message': 'System online'}), 200


# Request URL
@app.add_endpoint('/request', methods=['POST', 'GET'])
@app.add_endpoint('/request/<path:extra>', methods=['POST'])
def request_one(extra=None):
    request_token = request.headers.get('bearer')
    if not validate_token(token=request_token):
        abort(403)
    return jsonify({'message': 'Token is valid'}), 200


app.start_server(host='127.0.0.1', port=None, debug=False)