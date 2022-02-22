from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
import json
import subprocess
import sys
import mysql.connector
from werkzeug.utils import secure_filename
import os
# import magic
import urllib.request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepblue'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'deepblue'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
# db = SQLAlchemy(app)

UPLOAD_FOLDER = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=["POST", "GET"])
def hello():
    return render_template('fileupload.html')



@app.route("/upload", methods=['POST', 'GET'])
def upload():
    cur = mysql.connection.cursor()
    #cursor = mysql.connection.cursor()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form.get('first name')
        last = request.form.get('Last name')
        mail = request.form.get('email')
        addno = request.form.get('Admissionno')
        if 'fileInput' not in request.files:
            flash("No file part")
            return redirect(request.url)
        files = request.files.getlist('fileInput')


        # print(files)
        for file in files:
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                cur.execute("INSERT INTO deepblue_table(FirstName, Last_Name, Emailaddress, Admission_No, files_up) VALUES (%s, %s, %s ,%s, %s)",(name, last, mail, addno, filename))
                proc = subprocess.Popen(
                    'python author_script.py {}{} -p n -s n -m num'.format(UPLOAD_FOLDER, file.filename), shell=True,
                    stdout=subprocess.PIPE)

                mysql.connection.commit()
            print(file)
        cur.close()
        flash('File(s) successfully uploaded')
    return redirect('/')




if __name__ == "__main__":
  app.run(debug=True)

#app.run(debug=True)
