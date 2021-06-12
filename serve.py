import pymysql
from flask import Flask, render_template, request

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "Forward0606!",
    "db": "try_schema",
    "charset": "utf8"
}

app = Flask(__name__)
@app.route("/")
def home():
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM try_schema.comment")
            result = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return render_template("homepage.html", res = result)

@app.route("/add_comment",methods=["POST"])
def login():
    user_name = request.form.get("user")
    user_comment = request.form.get("comment")
    print(user_name)
    print(user_comment)
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO comment(name, comment)VALUES(%s, %s)"
            cursor.execute(command, (user_name, user_comment))
            # 儲存變更
            conn.commit()
            cursor.execute("SELECT * FROM try_schema.comment")
            result = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return render_template("homepage.html", res = result)

app.run(port=3508)