from flask import Flask, request, render_template, jsonify
import mysql.connector as sql

server = Flask(__name__)


def check(user):
    connection = sql.connect(
        user="root",
        password="Password",
        database="login"
    )
    cursor = connection.cursor()
    cursor.execute(f"select * from user where username='{user}'")
    data = cursor.fetchall()
    username = data[0][1]
    password = data[0][2]
    return username, password


def insert_into_database(name, username, password):
    connection = sql.connect(
        user="root",
        password="Password",
        database="login"
    )
    cursor = connection.cursor()
    cursor.execute(
        f"insert into user values('{name}','{username}','{password}');")
    connection.commit()
    cursor.close()
    connection.close()
    print("data insertion done")


@server.route("/")
def landingpage():
    print("index page loaded")
    return render_template("login.html")


@server.route("/signup", methods=["POST"])
def sigup():
    print("signup function called")
    data = request.get_json()
    name = data.get("name")
    user = data.get("username")
    password = data.get("pass")
    print(name, user, password)
    insert_into_database(name, user, password)
    return "<p></p>"


@server.route("/pagechange")
def main():
    return render_template("index.html")


@server.route("/welcome")
def hello():
    return "<p>Login Done</p>"


@server.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = data.get("username")
    password = data.get("pass")
    print(user, password)
    try:
        dbuser, dbpass = check(user)
        if user == dbuser and password == dbpass:
            print("login done")
            return jsonify({
                "is_exist": True,
                "status": True
            })
        else:
            return jsonify({
                "is_exist": True,
                "status": False
            })
    except:
        return jsonify({
            "is_exist": False
        })


server.run(debug=True)
