# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app

# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")

# functions/main.py

import functions_framework

@functions_framework.http
def example_function(request):
    """Responds to an HTTP request."""
    request_json = request.get_json(silent=True)
    if request_json and 'text' in request_json:
        text = request_json['text']
        return f"Server received: {text}"
    else:
        return "Hello from Python Cloud Function!"
