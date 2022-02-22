from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
import MySQLdb.cursors 
import mysql.connector

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepblue'

app.config['MYSQL_HOST']  = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'deepblue'
#db = SQLAlchemy(app)
mysql = MySQL(app)
# class deepblue(mysql.Model):
#
#     FirstName = db.Column(db.String(40), primary_key=True)
#     Last_Name = db.Column(db.String(45), nullable=False)
#     Emailaddress= db.Column(db.String(45), nullable=False)
#     Admission_No = db.Column(db.String(45), nullable=False)

@app.route("/databasecon", methods = ['GET', 'POST'])

def databasecon():
    if (request.method == 'POST'):
        '''Add entry to the database'''
       # details = request.form
        name = request.form.get('first name')
        last = request.form.get('Last name')
        mail = request.form.get('email')
        addno = request.form.get('Admissionno')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO deepblue_table(FirstName, Last_Name, Emailaddress, Admission_No) VALUES (%s, %s, %s ,%s)", (name, last, mail, addno ))
        mysql.connection.commit()
        cur.close()
        return 'success'
        #entry = deepblue(FirstName=name, Last_Name=last, Emailaddress=mail, Admission_No=addno)
        #db.session.add(entry)
       # db.session.commit()
    return render_template('databasecon.html')

#if __name__ == '_main_':
app.run(debug=True)