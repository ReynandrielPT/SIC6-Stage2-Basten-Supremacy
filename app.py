from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Koneksi ke MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/mydatabase")
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Flask berjalan di Vercel!"})

@app.route("/post_data", methods=["POST"])
def post_data():
    if request.method == "POST":
        try:
            data = request.json  # Ambil data JSON dari request
            collection.insert_one(data)  # Simpan ke MongoDB
            return jsonify({"status": "success", "data": data}), 201
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        return jsonify({"status": "error", "message": "Method Not Allowed"}), 405

# Handler untuk Vercel
def handler(request, *args, **kwargs):
    return app(request.environ, start_response)

if __name__ == "__main__":
    app.run(debug=True)
