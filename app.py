from flask import Flask, render_template, request, make_response, jsonify
import uuid

app = Flask(__name__)


class VideoGame:
    def __init__(self, title, platform):
        self.title = title
        self.platform = platform
        self.uuid = uuid

    def from_json(cls, videogame_entry):
        # Acquire json dictionary and output as string
        json_dict = json.loads(videogame_entry)
        return cls(**json_dict)


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
        if "title" in data.keys() and "platform" in data.keys():
            # Save title and platform dict values into videogame variable
            videogame = VideoGame(data["title"], data["platform"])

            # Generate and pass uuid property for each new videogame entry
            data["uuid"] = uuid.uuid4()
            data["resource-path"] = f'/videogame/{data["uuid"]}'
            data["status code"] = 201

            # Generate successful response for submission
            return jsonify(data)

        elif "title" in data.keys() and "platform" not in data.keys():
            missing_platform = {}

            # Store specific message in missing_title dict
            missing_platform["message"] = "Platform wasn't included in data set submission"
            missing_platform["endpoint"] = "/videogames"
            missing_platform["status code"] = 403

            print("Title wasn't included in data set submission")
            return jsonify(missing_platform)

        elif "title" not in data.keys() and "platform" in data.keys():
            missing_title = {}

            # Store specific message in missing_title dict
            missing_title["message"] = "Title wasn't included in data set submission"
            missing_title["endpoint"] = "/videogames"
            missing_title["status code"] = 403

            # Store specific message in missing_title dict

            print("Platform wasn't included in data set submission")
            return jsonify(missing_title)

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
