import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, url_for, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
show_login_error = False
sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()
try:
	
	cursor.execute("SELECT * FROM login")
	cursor.close()
	sqliteConnection.close()

except sqlite3.OperationalError:
	
	cursor.execute(''' CREATE TABLE login
         (uid TEXT PRIMARY KEY     NOT NULL,
         password           TEXT    NOT NULL);
         ''')
	print("CREATED")
	cursor.execute("INSERT INTO login VALUES('user1','123456')")
	cursor.execute("INSERT INTO login VALUES('user2','iloveyou')")
	cursor.execute("INSERT INTO login VALUES('user3','password')")
	cursor.execute("INSERT INTO login VALUES('admin','letmein')")
	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()


@app.route("/", methods=["GET"])
def dnm():
	if show_login_error == True:
		return render_template('index.html',asd='Wrong username or password')
	else:
		return render_template('index.html',asd='')
	

@app.route("/home", methods=["GET"])
def home():
	return render_template('home.html')



@app.route("/login", methods=["POST"])
def login():

	sqliteConnection = sqlite3.connect('sql.db')
	cursor = sqliteConnection.cursor()
	mydata = request.json

	uid = mydata["uid"]
	input_passwd = mydata["password"]
	query = f"SELECT * FROM login WHERE uid = '{uid}' AND password = '{input_passwd}'"
	print(query)
	cursor.execute(query)

	# Fetch and output result
	result = cursor.fetchall()
	print(result)
	if result != []:
		print("You're in!")
		cursor.close()
		if sqliteConnection:
			sqliteConnection.close()
			print('SQLite Connection closed')
			
		show_login_error = False
		return redirect(url_for("home"))
	else:
		cursor.close()
		if sqliteConnection:
			sqliteConnection.close()
			print('SQLite Connection closed')

		print("Wrong username or password!")
		show_login_error = True
		return redirect("/")
	
	

