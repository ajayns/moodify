from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from werkzeug import secure_filename

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/w')
def webcam():
  return render_template("webcam.html")

@app.route('/hello')
def hello():
  return "hello world"

@app.route('/star', methods=['GET'])
def get_all_stars():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify(output)

@app.route('/star/', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name': s['name'], 'distance': s['distance']}
  else:
    output = "No such name"
  return jsonify(output)

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id})
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify(output)

@app.route('/uploader', methods=['POST'])
def upload_file():
  f = request.files['file']
  f.save(secure_filename('1'))


if __name__ == '__main__':
  app.run(debug=True)
