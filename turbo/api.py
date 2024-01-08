from flask import *

# Create Flask
class FlaskAPI:
    def __init__(self, app_name):
        self.app = Flask(app_name)
        self.endpoints = {}

    def add_endpoint(self, route, methods):
        def decorator(handler):
            self.app.route(route, methods=methods)(handler)
            self.endpoints[route] = methods
            return handler
        return decorator

    def start_server(self, host='127.0.0.1', port=None, debug=False):
        self.app.run(host=host, port=port, debug=debug)