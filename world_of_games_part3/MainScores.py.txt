# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.
#
# Methods
# 1. score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML that will be as follows:
from flask import Flask, request


def score_server():
    app = Flask("something")

    @app.route('/whatismyscore', methods=['GET', 'POST', 'DELETE'])
    def hello():
        if request.method == 'GET':
            try:
                with open("Scores.txt") as myfile:
                    for line in myfile.readlines():
                        score = line
                myfile.close()
                return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{score}</div' \
                       f'></h1></body></html> '
            except FileNotFoundError as e:
                return f'<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{e.args}</div></h1></body></html> '
        elif request.method == 'POST':
            return "hello and welcome to the world of games"

    @app.route('/')
    def my_func():
        return "hello and welcome to the world of games"

    app.run(host="0.0.0.0", port=5001, debug=True)


score_server()
