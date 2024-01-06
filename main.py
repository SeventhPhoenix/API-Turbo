from API.builder import Flask_API, request, abort

app = Flask_API('Example Name')

# Home URL
@app.add_endpoint('/', methods=['GET'])
@app.add_endpoint('/<path:extra>', methods=['GET'])
def home(extra=None):
    return {'message': 'System online'}, 200

# Request URL
@app.add_endpoint('/request', methods=['GET'])
@app.add_endpoint('/request/<path:extra>', methods=['GET'])
def home(extra=None):
    token = request.headers.get('bearer')
    if token != str(221124):
        abort(503)
    return {'message': 'Token is valid'}, 200

app.run(host='0.0.0.0', port='33212', debug=False)