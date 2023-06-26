# from models import VideoGame
from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///media_backlog_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Videogame

# Run in terminal to connect database: export DATABASE_URL="postgresql:///media_backlog_api"

#     def from_json(cls, videogame_entry):
#         # Acquire json dictionary and output as string
#         json_dict = json.loads(videogame_entry)
#         return cls(**json_dict)


'''@app.route('/videogames')
def videogame_GET():
    return "Main page for video game directory."
'''

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
            # Save title and platform dict values into videogame variable. Constructor creates an empty arg. 
            videogame = Videogame()
            videogame.videogame_title = data["title"]
            videogame.videogame_platform = data["platform"]
            videogame.videogame_releasedate = data["releasedate"]
            videogame.videogame_publisher = data["publisher"]

            videogame.videogame_id = str(uuid.uuid4())
            db.session.add(videogame)
            db.session.commit()

            # Generate and pass uuid property for each new videogame entry
            data["uuid"] = videogame.videogame_id
            data["resource-path"] = f'/videogame/{data["uuid"]}'

            # SQLAlchemy. Review db.session.commit() func

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


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def info_query(uuid):
    # if uuid not in db, return a 400, bad request error
    entry_info = Videogame.query.get(uuid)
    if entry_info:
        return f"The requested ID is: {entry_info.videogame_id}"
    else:
        return "Entry not found."
# Successful GET Request: curl -X GET http://127.0.0.1:5000/videogames/88cb6cae-f55b-4f65-839c-ab58a5d88e91



if __name__ == '__main__':
    app.run()


# Successful POST: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"title":"Spiderman 2", "platform":"PlayStation"}'
# Inaccurate JSON file: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"name":"Spiderman 2", "platform":"PlayStation 2"}'
