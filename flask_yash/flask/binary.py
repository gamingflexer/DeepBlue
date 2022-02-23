from flask import Flask, render_template, request, flash, redirect
from flask import Flask, request, redirect, url_for, flash, render_template
from flask import *
import os, shutil
import app
import urllib.request
import zipfile
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
import json
import subprocess
import urllib.request
import MySQLdb.cursors
import sys
from flask_mysqldb import MySQL
import mysql.connector
from werkzeug.utils import secure_filename
from fileconversion import*
from modelspacy import*
import pandas as pd
from get_links import *
data = pd.read_csv("C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\BACKEND\\ML\\Datasets (UNCLEANED)\\not used\\TEST DATA (without NER).csv")
# import magic
import urllib.request
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binarydata = file.read()
    return binarydata
def convertBinaryToFile(binarydata,filename):
    with open(filename, 'wb') as file:
        file.write(binarydata)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepblue'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'deepbluecomp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
# db = SQLAlchemy(app)

UPLOAD_FOLDER = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ZIPPED = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\zip"
app.config['ZIPPED'] = ZIPPED
EXTRACTED = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\extracted"
app.config['EXTRACTED'] = EXTRACTED
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx', 'doc', 'rtf', 'odt','html', 'txt','zip'])

#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/', methods=["POST", "GET"])
def hello():
    return render_template('Homepage.html')

@app.route('/upload2', methods=["POST", "GET"])
def upload2():
    return render_template('upload2.html')


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    cur = mysql.connection.cursor()
    #cursor = mysql.connection.cursor()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
       # name = request.form.get('first name')
        #last = request.form.get('Last name')
        #mail = request.form.get('email')
        #addno = request.form.get('Admissionno')
        if 'files[]' not in request.files:
            flash("No file part")
            return redirect(request.url)
        files = request.files.getlist('files[]')
        print(files)
        val = 1

        # print(files)
       # enumerate(list)

        for file in files:
            print(file)

            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print(file.filename)
                name=((file.filename).rsplit('.'))[1]
                if(name=='zip'):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['ZIPPED'], filename))
                    zip_ref = zipfile.ZipFile(os.path.join(app.config['ZIPPED'], filename), 'r')
                    zip_ref.extractall(app.config['EXTRACTED'])
                    dir_list = os.listdir(app.config['EXTRACTED'])
                    print(dir_list)
                    for i in dir_list:
                        original="C:\\Users\\Yash\\PycharmProjects\\flask\\static\\extracted\\"+str(i)
                        x = original.rindex("\\")
                        y = original.index(".")
                        num = str(val)
                        val = val + 1
                        path = original[:x + 1] + "resume" + num + original[y:]
                        filerename = "resume" + num + original[y:]
                        os.rename(original, path)
                        # binary = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\"+filename
                        binartfile = convertToBinary(path)
                        #moving on to final folder
                        cur.execute("INSERT INTO deepbluecomp_table(files_path,binaryfiles_path) VALUES (%s, %s)",
                                    (filerename, binartfile))
                        print("------")
                        text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion(
                            path, num)
                        linkdedln, github, others = get_links(link)

                        cur.execute(
                            "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                            (text1 ,ftext,pincode,mailid,linkdedln,github,others,phone_number))
                        # model eval

                        #model(text)

                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for file_name in dir_list:
                        source ="C:\\Users\\Yash\\PycharmProjects\\flask\\static\\extracted\\"+ file_name
                        destination = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\" + file_name
                        shutil.move(source, destination)





                else:

                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    binary = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\" + filename
                    #file1 = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\2021-12-08.png"
                    x = binary.rindex("\\")
                    y = binary.index(".")

                    num = str(val)
                    val = val+1


                    path = binary[:x + 1] + "resume" + num + binary[y:]
                    filerename="resume" + num + binary[y:]
                    os.rename(binary, path)
                    #binary = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\"+filename
                    binartfile = convertToBinary(path)

                    cur.execute("INSERT INTO deepbluecomp_table(files_path,binaryfiles_path) VALUES (%s, %s)",(filerename, binartfile))
                    print("------")
                    text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion(
                        path, num)
                    linkdedln, github, others = get_links(link)

                    cur.execute(
                        "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                        (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))
                    # model eval

                    #model(text)
                #model(data[1])



                #proc = subprocess.Popen('python author_script.py {}{} -p n -s n -m num'.format(UPLOAD_FOLDER, file.filename), shell=True,stdout=subprocess.PIPE)

    mysql.connection.commit()
            #print(file)
    cur.close()
    flash('File(s) successfully uploaded')
    #return redirect('/upload')
    return render_template('table2.html')

@app.route("/delete")
def delete():
    dirzip_list = os.listdir(app.config['ZIPPED'])

    for zipfileli in dirzip_list:

        os.remove("C:\\Users\\Yash\\PycharmProjects\\flask\\static\\zip\\" + zipfileli)

    folder = 'C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


    return render_template('upload2.html')

@app.route('/table', methods=["POST", "GET"])
def table():
    table_li=[]

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM list')
    #name,education,skills,experience,email
    print(result)
    if result > 0:
        row = cur.fetchall()
        print(row)
        for dict in row:
            table_li.append(list(dict.values()))
        print(table_li)









    return render_template('table2.html',row=table_li)


if __name__ == "__main__":
  app.run(debug=True)

#app.run(debug=True)
