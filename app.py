# from models import VideoGame
from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///media_backlog_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import VideoGame

# Run in terminal to connect database: export DATABASE_URL="postgresql:///media_backlog_api"

#     def from_json(cls, videogame_entry):
#         # Acquire json dictionary and output as string
#         json_dict = json.loads(videogame_entry)
#         return cls(**json_dict)


@app.route('/videogames')
def videogame_GET():
    return "Main page for video game directory."


@app.route('/videogames', methods=['POST'])
def videogame_POST():
    # try:
    if request.is_json:
        # Process the json data from the message body and store in data variable
        data = request.get_json()

        # Evaluate if key in data set
        error_message = {}
        error_message["endpoint"] = "/videogames"

        if "title" in data.keys() and "platform" in data.keys():
            # Save title and platform dict values into videogame variable
            videogame = VideoGame(data["title"], data["platform"])

            # Generate and pass uuid property for each new videogame entry
            data["uuid"] = uuid.uuid4()
            data["resource-path"] = f'/videogame/{data["uuid"]}'

            # Generate successful response for submission
            return jsonify(data), 201

        if "title" not in data.keys():
            error_message["message"] = "Title wasn't included in data set submission"
            return jsonify(error_message), 400

        elif "platform" not in data.keys():
            error_message["message"] = "Platform wasn't included in data set submission"
            return jsonify(error_message), 400

        else:
            return 'Request not being understood. Check previous if and elif statements'

    # Successful POST: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"title":"Spiderman 2", "platform":"PlayStation"}'
    # Inaccurate JSON file: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"name":"Spiderman 2", "platform":"PlayStation 2"}'


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def unique_info(uuid):
    assert resource == request.view_args['uuid']
    return "Pull specific info on video games in database."


if __name__ == '__main__':
    app.run()

# Import and register VideoGame model (Moved below the db object due to issues with initialization)
# from app import db