from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/videogames')
def index():
    return "Main page for video game directory."


@app.route('/videogames', methods=['GET', 'POST'])
def info_pull(resource):
    assert resource == request.view_args['resource']
    return "Pull general information on video games that are being requested."


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def unique_info(resource):
    assert resource == request.view_args['resource']
    return "Pull specific info on video games in database."


if __name__ == '__main__':
    app.run()
