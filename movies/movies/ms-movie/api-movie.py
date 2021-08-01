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

@app.route("/movies", methods=['GET'])
def home():
    movies = db.basics.find()
    return Response(json.dumps([movie for movie in movies], default=json_serial),mimetype='application/json')

@app.route("/movies/<filmeId>", methods=['GET'])
def find_one(filmeId):
    movie = db.basics.find_one({"tconst": filmeId})
    return Response(json.dumps(movie,default=json_serial),mimetype='application/json')


@app.route("/movies/rate/<filmeId>", methods=['GET'])
def find_movie_rate(filmeId):
    movies = db.basics.aggregate([{
        '$lookup': {
            'from': 'ratings',
            'localField': 'tconst',
            'foreignField': 'tconst',
            'as': 'rate'
        }
    },
    {
        '$match': {'tconst':filmeId}
    }])
    return Response(json.dumps([movie for movie in movies], default=json_serial),mimetype='application/json')

@app.route('/movies', methods=['POST'])
def add_movie():
  movie = db.basics
  genres = request.json['genres']
  startYear = request.json['startYear']
  runtimeMinutes = request.json['runtimeMinutes']
  originalTitle = request.json['originalTitle']
  endYear = request.json['endYear']
  tconst = request.json['tconst']
  primaryTitle = request.json['primaryTitle']
  titleType = request.json['titleType']
  isAdult = request.json['isAdult']
  movie_id = movie.insert({'genres': genres, 'startYear': startYear,'runtimeMinutes': runtimeMinutes,
   'originalTitle': originalTitle,'endYear': endYear, 'tconst': tconst,'primaryTitle': primaryTitle,
   'titleType': titleType, 'isAdult': isAdult})
  new_movie = movie.find_one({'_id': movie_id })
  output = {'genres': new_movie['genres'], 'startYear': new_movie['startYear'],'runtimeMinutes': new_movie['runtimeMinutes'],
   'originalTitle': new_movie['originalTitle'],'endYear': new_movie['endYear'], 'tconst': new_movie['tconst'],'primaryTitle': new_movie['primaryTitle'],
   'titleType': new_movie['titleType'], 'isAdult': new_movie['isAdult']}
  return jsonify({'result' : output})

@app.route("/movies/<filmeId>", methods=['DELETE'])
def delete_movie(filmeId):
    movie = db.basics.delete_one({'tconst': filmeId})
    return movie.raw_result

if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)