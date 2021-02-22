from flask import Flask, request, jsonify, make_response
from train_model import run_model

app = Flask(__name__)

@app.route("/recommendations", methods=["POST", "OPTIONS"])
def api_create_order():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "POST":
        my_classes = [str(c) for c in request.json['in_cart']]
        result = run_model(my_classes) if len(my_classes) > 0 else []
        return _cors_actual_response(jsonify(result))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _cors_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
