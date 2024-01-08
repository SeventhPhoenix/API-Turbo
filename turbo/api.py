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

    def start_server(self, host='0.0.0.0', port=5000, debug=False):
        self.app.run(host=host, port=port, debug=debug)