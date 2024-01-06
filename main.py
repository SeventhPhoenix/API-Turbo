from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Service Unavailable'}

def start_server():
    app.run(host='0.0.0.0', port=23211)

start_server()