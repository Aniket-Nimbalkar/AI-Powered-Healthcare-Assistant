from flask import Flask, request, jsonify
from flask_cors import CORS 
from search_engine import search_medical_info

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query", "")
    response = search_medical_info(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
