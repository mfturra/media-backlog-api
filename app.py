from flask import Flask, render_template, request

app = Flask(__name__)

# Videogame Class Definition
# Initialize an instance of Class

# Example
v = {
    "name": "Spiderman 2",
    "platform": "PlayStation"
}


class VideoGame:
    def __init__(self, name, platform):
        self.gameName = name
        self.gamePlatform = platform


@app.route('/videogames')
def index():
    return "Main page for video game directory."


@app.route('/videogames', methods=['GET', 'POST'])
def info_pull(resource):
    assert resource == request.view_args['resource']

    if request.method == "POST":
        try:
            @classmethod
            def from_json(cls, videogame_entry):
                # Acquire json dictionary and output as string
                json_dict = json.loads(videogame_entry)
                return cls(**json_dict)

            def __repr__(self):
                return f'<Success! A new entry has been included for {self.gameName} on {self.gamePlatform}>'

            # curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"name": "Spiderman 2","platform": "PlayStation"}'

            videogame_entry = '''{
                "name": "Spiderman 2",
                "platform": "PlayStation"
                }'''

            videogame = VideoGame.from_json(videogame_entry)
            print(videogame)

            '''else:
                print(f"Error. Database wasn't updated properly.")'''

        except ValueError as e:
            print("Error: ", e)
    return "Pull general information on video games that are being requested."


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def unique_info(resource):
    assert resource == request.view_args['resource']
    return "Pull specific info on video games in database."


if __name__ == '__main__':
    app.run()
