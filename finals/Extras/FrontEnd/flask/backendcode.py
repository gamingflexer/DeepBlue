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
app.config['MYSQL_DB'] = 'deepbluecomp'
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
    return render_template('back.html')


@app.route('/back', methods = ['GET', 'POST'])

def databasecon():
    if (request.method == 'POST'):
        '''Add entry to the database'''
       # details = request.form
        raw = parser.from_file("C:\\Users\\Yash\\OneDrive\\Desktop\\SeM3\\linkdien.pdf")
        #print(raw['content'])
        text = raw['content']
        #print(text)
        sampletext="Hello this is yash wakekar yashwakekar231@gmail.com with 8369879473 jaywant patil bluiding plot no 127 near hanuman mandir shiravane gaon nerul navi mumbai 400706"
        #print(email(text)) working
        #print(url(text))  #working
        #phone_number = get_phone_numbers(sampletext) #working
        #print(phone_number)
        #extracted_text = {}
        #extracted_text['Phone number'] = phone_number
        #print(extracted_text)
        #print(data_grabber(text))   #working
        #print(get_human_names(sampletext))                                   #getting none
        #print(human_name(sampletext))                                           #getting none
        #print(address_grabber(sampletext))                               #not getting op empty list
        #print(pincode_grabber(sampletext))                                #not given anything

        text1=pre_process1_rsw1(sampletext)  #working
        print(text1)
        #print(pre_process2_rsw(text))                                    # iterable error
        #print(pre_process3_rpm(text))                                     #error not imp
        #print(remove_hexcode_rhc(text1)) working

        cur = mysql.connection.cursor()
       # cur.execute("INSERT * FROM records WHERE email LIKE %s", [search])
        cur.execute("INSERT INTO datastore (data) VALUES (%s)", (text,))
        mysql.connection.commit()
        cur.close()
        return 'success'
        #entry = deepblue(FirstName=name, Last_Name=last, Emailaddress=mail, Admission_No=addno)
        #db.session.add(entry)
       # db.session.commit()
    return redirect('/')

#if __name__ == '_main_':
app.run(debug=True)

#from tika import parser
#raw = parser.from_file("C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\linkdien.pdf")
#print(raw['content'])
#text = raw['content']
#print(text)