from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import engine

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/health")
def health():
    return jsonify ({"status": "Ok"})

@app.route("/api/recommendation", methods = ['GET'])
def recommendation():
        title = request.args.get('title')
        result = engine.get_recommendation(title)
        if(result == "No Movies Found"):
            return jsonify({"status":"error", "message": "No Movies Found"}), 404
        
        return jsonify({"movies" : result})
    
if __name__ == "__main__":
        app.run(port=5001, debug=True, host="0.0.0.0")