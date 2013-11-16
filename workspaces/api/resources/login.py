from flask import abort
from flask.ext.security.utils import verify_and_update_password

from .resource import Resource
from ...models import User


class LoginResource(Resource):

    def post(self):
        data = self.post_data()

        # Check for proper request content
        if not 'username' and 'password' in data:
            abort(400, "Must include 'username' and 'password' parameters.")

        username = data['username']
        password = data['password']

        # Check that user exists
        u = User.query.filter_by(username=username).first()
        if (not u or not u.is_active() or
                not verify_and_update_password(password, u)):
            abort(401, "Invalid password or username.")

        return {"token": u.get_auth_token()}