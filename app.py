from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hes4dp3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)


@app.route('/')
def home():


    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():


    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive, 'comment' : comment_receive}
    db.singer.insert_one(doc)





    return jsonify({'msg':'저장 완료' })


@app.route("/homework", methods=["GET"])
def homework_get():


    singers = list(db.singer.find({}, {'_id': False}))
    return jsonify({'singer':singers})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
