from flask import Flask
from flask import jsonify
from flask import request
import pymongo

app = Flask(__name__)

# connecting to mongo client
client = pymongo.MongoClient('localhost', 27017)
db = client["gurudeva"]


@app.route('/jai_sriram', methods=['GET'])
def first_function():
    return jsonify({"name": "jai sriram"})


@app.route('/sriram', methods=['POST'])
def second_function():
    return jsonify(request.json)


@app.route('/mongodb', methods=['GET'])
def student_fetch():
    data = db.students.find({}, {"_id": 0})
    return jsonify(list(data))


@app.route('/mongodb_post', methods=['POST'])
def student_post():
    data = db.students.insert_many(request.json)
    return student_fetch()


if __name__ == "__main__":
    app.run()
# host="120.0.0.1", port=9192

# mongodb
"""
mongodb://localhost:27017
"""
