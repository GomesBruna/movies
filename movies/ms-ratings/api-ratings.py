#!/usr/bin/env python

from flask import Flask, request, jsonify,Response
from flask_pymongo import PyMongo
import json
from bson import ObjectId

def json_serial(obj):
    if isinstance(obj, ObjectId):
       return str(obj)
    return json.JSONEncoder.default(self, obj)



app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://db:27017/movies")
db = mongodb_client.db

@app.route("/")
def hello():
    return "API Funcionando!\n"

@app.route("/ratings")
def home():
    rates = db.ratings.find()
    return Response(json.dumps([rate for rate in rates], default=json_serial),mimetype='application/json')


@app.route("/ratings/<filmeId>")
def find_one(filmeId):
    rate = db.ratings.find_one({"tconst": filmeId})
    return Response(json.dumps(rate,default=json_serial),mimetype='application/json')

@app.route('/ratings', methods=['POST'])
def add_rate():
  movie = db.ratings
  numVotes = request.json['numVotes']
  tconst = request.json['tconst']
  averageRating = request.json['averageRating']
  
  rate_id = movie.insert({'numVotes': numVotes, 'tconst': tconst,'averageRating': averageRating})
  new_rate = movie.find_one({'_id': rate_id })
  output = {'numVotes': new_rate['numVotes'], 'tconst': new_rate['tconst'],'averageRating': new_rate['averageRating']}
  return jsonify({'result' : output})

@app.route("/ratings/<filmeId>", methods=['DELETE'])
def delete_rate(filmeId):
    rate = db.ratings.delete_one({'tconst': filmeId})
    return rate.raw_result


if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)