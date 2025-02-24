from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId for conversion

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = "mongodb+srv://BastenSupremator:123@cluster0.dowjb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/post_data", methods=["POST"])
def post_data():
    try:
        data = request.json
        result = collection.insert_one(data)  # Insert to MongoDB
        
        # Convert ObjectId to string before returning JSON
        data["_id"] = str(result.inserted_id)  

        return jsonify({"status": "success", "data": data}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
