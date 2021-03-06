# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb
import secrets

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Avengers!@2021"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_DB"] = "user_schema"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config['SECRET_KEY'] = "lovely"

db = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = str(request.form['username'])
            print(type(username))
            password = str(request.form['password'])
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            # conn = db.connect()
            # cursor = conn.cursor()
            cursor.execute("SELECT * FROM login_info WHERE username=%s and password=%s", (username, password))
            info = cursor.fetchone()
            if info is not None:
                if info['username'] == username and info['password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for('profile'))
                else:
                    return redirect(url_for('login'))

    return render_template('Login.html')


@app.route('/register', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form and "four" in request.form and "five" in request.form:
            firstname = request.form['one']
            lastname = request.form['two']
            email = request.form['three']
            username = request.form['four']
            password = request.form['five']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO user_schema.login_info(firstname, lastname, email, username, password)"
                        "VALUES(%s,%s,%s,%s,%s)", (firstname, lastname, email, username, password))
            db.connection.commit()
            return redirect(url_for('index'))
    return render_template('Register.html')


# @app.route('/register')
# def register():
#     return render_template('Register.html')


@app.route('/new/profile')
def profile():
    if session['loginsuccess']:
        return render_template('Profile.html')


@app.route('/new/profile/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('index'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
