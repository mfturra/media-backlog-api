from Flask import flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Main page for video game inclusion."


@app.route('/{resource}', methods=['GET', 'POST'])
def info_pull():
    return "Pull general information on video games that are being requested."


@app.route('/{resource}/uuid', methods=['GET', 'PATCH', 'DELETE'])
def unique_info():
    return "Pull specifci info on video games in database."
