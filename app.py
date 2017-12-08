#!flask/bin/python
from flask import Flask, jsonify, json, abort

app = Flask(__name__)

jData = json.loads(open('./friends.json').read())
friends = jData["friends"]

@app.route('/', methods=['GET'])
def get_all():
    return jsonify({'friends': friends})

@app.route('/friends', methods=['GET'])
def get_tasks():
    return jsonify({'friends': friends})

@app.route('/friends/<string:friend_age>', methods=['GET'])
def get_friend_age(friend_age):
    friend = [friend for friend in friends if friend['age'] == friend_age]
    if len(friend) == 0:
        abort(404)
    return jsonify({'friend': friend[0]})

@app.route('/friends/<string:friend_title>', methods=['GET'])
def get_friend_title(friend_title):
    friend = [friend for friend in friends if friend['title'] == friend_title]
    if len(friend) == 0:
        abort(404)
    return jsonify({'friend': friend[0]})

@app.route('/friends/name/<string:friend_name>', methods=['GET'])
def get_friend_name(friend_name):
    friend = [friend for friend in friends if friend['firstName'] == friend_name]
    if len(friend) == 0:
        abort(404)
    return jsonify({'friend': friend[0]})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
