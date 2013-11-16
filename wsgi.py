from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from workspaces import api

application = DispatcherMiddleware(api.create_app())

if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, application, use_reloader=True, use_debugger=True)