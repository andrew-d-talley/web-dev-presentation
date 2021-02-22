from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/recommendations", methods=["POST", "OPTIONS"])
def api_create_order():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "POST":
        print(request.json['in_cart'])
        return _cors_actual_response(jsonify([1101]))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _cors_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
