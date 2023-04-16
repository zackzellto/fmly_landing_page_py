from flask import Flask, request, jsonify, abort
import uuid
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo.mongo_client import MongoClient
import os

app = Flask(__name__)

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

DB_URL = os.environ.get('CONNECTION_STRING')

# Create a new client and connect to the server
client = MongoClient(DB_URL)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

email_submissions = []


@app.route('/api/waitlist', methods=['GET'])
def get_emails():
    return jsonify(email_submissions)


@app.route('/api/waitlist', methods=['POST'])
def create_email():
    email = request.json.get('email')
    if not email:
        abort(400, {'error': 'Email is required'})
    new_submission = {
        'id': str(uuid.uuid4()),
        'email': email,
        'timestamp': datetime.now().isoformat()
    }
    email_submissions.append(new_submission)
    return jsonify(new_submission), 201


@app.route('/api/waitlist/<string:id>', methods=['GET'])
def get_email(id):
    submission = next(
        (submission for submission in email_submissions if submission['id'] == id), None)
    if not submission:
        abort(404, {'error': 'Email submission not found'})
    return jsonify(submission)


@app.route('/api/waitlist/<string:id>', methods=['PUT'])
def update_email(id):
    submission = next(
        (submission for submission in email_submissions if submission['id'] == id), None)
    if not submission:
        abort(404, {'error': 'Email submission not found'})
    email = request.json.get('email')
    if not email:
        abort(400, {'error': 'Email is required'})
    submission['email'] = email
    submission['timestamp'] = datetime.now().isoformat()
    return jsonify(submission)


@app.route('/api/waitlist/<string:id>', methods=['DELETE'])
def delete_email(id):
    submission = next(
        (submission for submission in email_submissions if submission['id'] == id), None)
    if not submission:
        abort(404, {'error': 'Email submission not found'})
    email_submissions.remove(submission)
    return '', 204


app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
