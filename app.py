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

@app.route('/videogames', methods=['GET'])
def videogame_main():
    query_all = db.session.query(Videogame).all()

    # Empty list to store all entries
    all_entries = []

    # Iterate over all query_all results
    for entry in query_all:
        entry_info = {
            "title": entry.videogame_title,
            "platform": entry.videogame_platform,
            "releasedate": entry.videogame_releasedate,
            "publisher": entry.videogame_publisher
        }
        
        # Combine all entries into the all_entries list
        all_entries.append(entry_info)

    response = {
        "items": all_entries
    }
    return jsonify(all_entries)


@app.route('/videogames', methods=['POST'])
# Successful POST request example: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"title":"Spiderman 2", "platform":"PlayStation", "releasedate": "2004-06-28", "publisher": "Activision"}'
# Inaccurate JSON example: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"name":"Spiderman 2", "platform":"PlayStation 2"}'

def videogame_POST():
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
            return jsonify(data), 201 # Created

        if "title" not in data.keys():
            error_message["message"] = "Title wasn't included in data set submission"
            return jsonify(error_message), 400 # Bad request

        elif "platform" not in data.keys():
            error_message["message"] = "Platform wasn't included in data set submission"
            return jsonify(error_message), 400 # Bad request

        else:
            return 'Request not being understood. Check previous if and elif statements'


@app.route('/videogames/<uuid>', methods=['GET'])
# GET Request Example: curl -X GET http://127.0.0.1:5000/videogames/88cb6cae-f55b-4f65-839c-ab58a5d88e91
# Query for UUID entry in the Videogame Database
def info_query(uuid):
    entry_info = db.session.query(Videogame).filter(Videogame.videogame_id == uuid).first()
    if entry_info:
        # videogame_query = "The requested ID is: {entry_info.videogame_id}\nThe title is: {entry_info.videogame_title}\nThe platform is: {entry_info.videogame_platform}\nThe release date is: {entry_info.videogame_releasedate}\nThe publisher is: {entry_info.videogame_publisher}"
        return jsonify(entry_info), 200 # OK

    else:
        query_notfound = {"message": "Entry not found."}
        return jsonify(query_notfound), 400 # Bad request

@app.route('/videogames/<uuid>', methods=['DELETE'])
# DELETE Request Example: curl -X DELETE http://127.0.0.1:5000/videogames/88cb6cae-f55b-4f65-839c-ab58a5d88e91
# Query for UUID entry and delete entry
def delete_entry(uuid):
    entry_info = db.session.query(Videogame).filter(Videogame.videogame_id == uuid).first()
    if entry_info:
        db.session.delete(entry_info)
        db.session.commit()
        query_deleted = {"message": "Entry has been deleted."}
        return jsonify(query_deleted), 200 # OK
    else:
        query_notfound = {"message": "Entry not found."}
        return jsonify(query_notfound), 400 # Bad request


if __name__ == '__main__':
    app.run(host='0.0.0.0')