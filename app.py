from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://BastenSupremator:123@cluster0.dowjb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Flask berjalan di Render!"})

@app.route("/post_data", methods=["POST"])
def post_data():
    try:
        data = request.json  # Ambil data dari request
        collection.insert_one(data)  # Simpan ke MongoDB
        return jsonify({"status": "success", "data": data}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
