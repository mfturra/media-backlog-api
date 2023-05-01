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
