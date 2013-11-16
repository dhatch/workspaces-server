from workspaces import api
from workspaces.models import *

app = api.create_app()
ctx = app.test_request_context()

def pre_rq():
    ctx.push()
    app.preprocess_request()

def post_rq():
    app.process_response(app.response_class())
    ctx.pop()

import code
code.interact(local=locals())