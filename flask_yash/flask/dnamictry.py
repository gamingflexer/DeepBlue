import tika
from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
from tika import parser
from preprocessing import*
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
import MySQLdb.cursors
import mysql.connector

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepbluecomp'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'studentdata'
#db = SQLAlchemy(app)
mysql = MySQL(app)
# class deepblue(mysql.Model):
#
#     FirstName = db.Column(db.String(40), primary_key=True)
#     Last_Name = db.Column(db.String(45), nullable=False)
#     Emailaddress= db.Column(db.String(45), nullable=False)
#     Admission_No = db.Column(db.String(45), nullable=False)
@app.route('/', methods=["POST", "GET"])
def hello():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM yashdaa ')
    if result > 0:
        row = cur.fetchall()
        print(row)


    return render_template('statistics.html',row=row)

if __name__ == "__main__":
  app.run(debug=True)
