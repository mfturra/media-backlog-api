from flask import Flask, render_template, request

app = Flask(__name__)

# Videogame Class Definition
# Initialize an instance of Class


class VideoGame:
    def __init__(self, title, platform):
        self.title = title
        self.platform = platform

    def from_json(cls, videogame_entry):
        # Acquire json dictionary and output as string
        json_dict = json.loads(videogame_entry)
        return cls(**json_dict)


@app.route('/videogames')
def videogame_GET():
    return "Main page for video game directory."


@app.route('/videogames', methods=['POST'])
def videogame_POST():
    try:
        if request.is_json:
            # Process the json data from the message body and store in data variable
            data = request.get_json()

            # Store data content in VideoGame class
            videogame = VideoGame(data["title"], data["platform"])

            # Produce an output to the server on the terminal side to know that the job was done.
            return f"Successful submission of {videogame.title} and {videogame.platform} to the database."
    except:
        print(f"Error. Database wasn't updated properly.")
        return f"Error. Database wasn't updated properly."

    # curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"title":"Spiderman 2", "platform":"PlayStation"}'

    '''videogame = VideoGame.from_json(videogame_entry)
    print(videogame)'''

    return "Pull general information on video games that are being requested."


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def unique_info(uuid):
    assert resource == request.view_args['uuid']
    return "Pull specific info on video games in database."


if __name__ == '__main__':
    app.run()
