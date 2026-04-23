import mysql.connector as sql


def check(user):
    connection = sql.connect(
        user="root",
        password="Password",
        database="login"
    )
    cursor = connection.cursor()
    cursor.execute(f"select * from user where username='{user}'")
    data=cursor.fetchall()
    username=data[0][1]
    password=data[0][2]
    return username,password


check("aleice123")
