from flask import Flask, request, jsonify, abort
import uuid
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
from pymongo.collection import Collection
from flask_cors import CORS

load_dotenv(find_dotenv())

app = Flask(__name__)

CORS(app)
# Create the Swagger UI blueprint
# URL for exposing Swagger UI (without trailing '/')
SWAGGER_URL = '/swagger'

# URL for exposing OpenAPI spec (without trailing '/')
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fmly Landing Page API"
    }
)

DB_URL = os.environ.get("CONNECTION_STRING")

# Create a new client and connect to the server
client = MongoClient(DB_URL)

databases = client.list_database_names()
fmly_waitlist_db = client['Fmly_Waitlist_DB']
collections = fmly_waitlist_db.list_collection_names()

print(collections)


# class Waitlist(Collection):
#     def __init__(self, db):
#         super().__init__(db, 'waitlist')

#     def add_user(self, email):
#         self.insert_one({'email': email})

#     def remove_user(self, email):
#         self.delete_one({'email': email})

#     def get_users(self):
#         return self.find({}, {'_id': 0, 'email': 1})


# email_submissions = []


# @app.route('/api/waitlist', methods=['GET'])
# def get_emails():
#     return jsonify(email_submissions)


# @app.route('/api/waitlist', methods=['POST'])
# def create_email():
#     email = request.json.get('email')
#     if not email:
#         abort(400, {'error': 'Email is required'})
#     new_submission = {
#         'id': str(uuid.uuid4()),
#         'email': email,
#         'timestamp': datetime.now().isoformat()
#     }
#     email_submissions.append(new_submission)
#     return jsonify(new_submission), 201


# @app.route('/api/waitlist/<string:id>', methods=['GET'])
# def get_email(id):
#     submission = next(
#         (submission for submission in email_submissions if submission['id'] == id), None)
#     if not submission:
#         abort(404, {'error': 'Email submission not found'})
#     return jsonify(submission)


# @app.route('/api/waitlist/<string:id>', methods=['PUT'])
# def update_email(id):
#     submission = next(
#         (submission for submission in email_submissions if submission['id'] == id), None)
#     if not submission:
#         abort(404, {'error': 'Email submission not found'})
#     email = request.json.get('email')
#     if not email:
#         abort(400, {'error': 'Email is required'})
#     submission['email'] = email
#     submission['timestamp'] = datetime.now().isoformat()
#     return jsonify(submission)


# @app.route('/api/waitlist/<string:id>', methods=['DELETE'])
# def delete_email(id):
#     submission = next(
#         (submission for submission in email_submissions if submission['id'] == id), None)
#     if not submission:
#         abort(404, {'error': 'Email submission not found'})
#     email_submissions.remove(submission)
#     return '', 204


app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
