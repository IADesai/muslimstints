# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from flask import Flask, request, jsonify
from firebase_functions import https_fn
from firebase_admin import initialize_app, credentials, firestore
from firebase_service import add_user_to_firestore

cred = credentials.Certificate("path/to/your-service-account-key.json")  # Replace with your JSON key path
initialize_app(cred)

# Firestore client
db = firestore.client()

def add_user_to_firestore(user_data):
    """Add user data to Firestore."""
    try:
        user_ref = db.collection('users').document(user_data['uid'])
        user_ref.set(user_data)
        return {"success": True, "message": "User added successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}

app = Flask(__name__)

@app.route('/add-user', methods=['POST'])
def add_user():
    """API to add a user to Firestore."""
    try:
        user_data = request.json
        response = add_user_to_firestore(user_data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)