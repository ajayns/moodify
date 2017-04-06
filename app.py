# Third-party imports
from flask import Flask, jsonify, request, render_template, redirect
from flask_pymongo import PyMongo
from werkzeug import secure_filename


# Initialize app and database
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'moodmusic'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/moodmusic'

mongo = PyMongo(app)

# Setup routes
@app.route('/')
def index():
  return redirect("/player")

@app.route('/player')
def player():
  return render_template("player.html")

@app.route('/cam')
def cam():
  return render_template("cam.html")

@app.route('/music', methods=['GET'])
def music():
  songs = mongo.db.songs
  output = []
  for s in songs.find():
    output.append({'title' : s['title'], 'album': s['album'], 'artist' : s['artist'], 'albumart' : s['albumart'], 'url' : s['url']})
  return jsonify(output)

@app.route('/emotion', methods=['GET', 'POST'])
def emotion():
  return

# Main
if __name__ == '__main__':
  app.run(debug=True)
