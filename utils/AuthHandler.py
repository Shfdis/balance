import json

from flask import abort


class AuthHandler:
    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.password = data["password"]
    def check_login(self, request):
        if request.args.get('password') != self.password:
            abort(401)


AUTH_HANDLER = AuthHandler()