from flask import Flask, request, jsonify, abort
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from pymongo.collection import Collection
from flask_cors import CORS
from datetime import datetime
import os

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

email_submissions = []


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.route('/api/waitlist', methods=['POST'])
def join_waitlist():
    form_data = {
        # 'id': str(uuid.uuid4()),
        'email': request.json['email'],
        'timestamp': get_timestamp(),
    }

    result = fmly_waitlist_db.collections.insert_one(form_data)
    if not result:
        abort(400, {'error': 'Email is required'})
    email_submissions.append(form_data)
    return jsonify({'success': True}), 201


@app.route('/api/waitlist', methods=['GET'])
def get_all_emails():
    email_submissions = fmly_waitlist_db.collections.find()
    return jsonify(email_submissions)


@app.route('/api/waitlist/{id}', methods=['GET'])
def get_email_by_id(id):
    email = fmly_waitlist_db.collections.find_one(id)
    return jsonify(email)


@app.route('/api/waitlist/{id}', methods=['UPDATE'])
def update_email_by_id(id):
    update = fmly_waitlist_db.collections.update_one(id)
    if update:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


@app.route('/api/waitlist/{id}', methods=['DELETE'])
def delete_email_by_id(id):
    delete = fmly_waitlist_db.collections.delete_one(id)
    if delete:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
