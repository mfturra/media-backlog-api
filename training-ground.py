import json

# Creation of a Video Game class


class VideoGame:
    # Define the attributes of the object
    def __init__(self, name, platform):
        self.gameName = name
        self.gamePlatform = platform

    # Create a method that acquires json and converts to an obj. Json will usually come in as a string.
    @classmethod
    def from_json(cls, videogame_entry):
        # Acquire json dictionary and output as string
        json_dict = json.loads(videogame_entry)
        return cls(**json_dict)

    def __repr__(self):
        return f'<New entry is for {self.gameName} on {self.gamePlatform}>'


videogame_entry = '''{
    "name": "Spiderman 2",
    "platform": "PlayStation"
    }'''

videogame = VideoGame.from_json(videogame_entry)
print(videogame)


@app.route('/videogames', methods=['POST'])
def videogame_POST():
    try:
        if request.is_json:
            # Process the json data from the message body and store in data variable
            data = request.get_json()

            # Validate json data
            try:
                isinstance(data, VideoGame)

                # Store data content in VideoGame class
                videogame = VideoGame(data["title"], data["platform"])

                # Produce an output to the server on the terminal side to know that the job was done.
                return f"Successful submission of {videogame.title} and {videogame.platform} to the database."
            except ValueError as err:
                print(f"Error. Database wasn't updated properly.")

    except ValueError as err:
        print(f"Error. Database wasn't updated properly.")
        return f"Error. Database wasn't updated properly."
