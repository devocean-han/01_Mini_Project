## 서버로의 연결 세팅
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

## 클라우드 DB로의 연결 세팅
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ecmqblf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
client2 = MongoClient('mongodb+srv://ckdals1994:ckdalsla94@cluster0.xtrzoeq.mongodb.net/Cluster0?retryWrites=true&w=majority')
db2 = client2.mini_project

import datetime

@app.route('/')
def home():
    return render_template("02index_personal.html")

@app.route('/toHome')
def test():
    return render_template('04index_my.html')

@app.route("/api/get_comments", methods=["GET"])
def get_comments():
    comments_list1 = list(db.miniProject.find({}, {'_id':False}))


    # => 이거 콘솔에서는 잘 되는데 왜 여기서는 안되ㅣㅣㅣㅣㅣㅣㅣㅣ....ㅠㅠ
    # 참고: https://stackoverflow.com/questions/21446278/sort-python-list-of-dictionaries-by-key-if-key-exists
    # comments = comments_list[:].sort(key=lambda x: ('time' not in x, x.get('time', None)))
    comments_list2 = list(db2.guest.find({}, {'_id':False}))
    # comments = comments_list2 + comments_list1
    comments = comments_list1[5:]
    print(type(comments[0]['time']), comments[0]['time'])
    comments.sort(key=lambda k: ("time" not in k, k.get("time", None)))

    return jsonify({'msg': '코멘트 불러오기를 완료했습니다', 'comments_list': comments})

@app.route("/api/post_comment", methods=["POST"])
def post_comment():
    name = request.form['name_given']
    comment = request.form['comment_given']
    time = datetime.strptime(datetime.datetime.now("%Y-%m-%d %H:%M"))
    print(type(time), time)

    doc = {
        'name': name,
        'comment': comment,
        'time': time
    }
    db.miniProject.insert_one(doc)
    # db2.guest.insert_one(doc)
    return jsonify({'msg': '코멘트 등록이 완료되었습니다'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)