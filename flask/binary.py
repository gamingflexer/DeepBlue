from flask import Flask, render_template, request, flash, redirect
from flask import *
import os
import shutil
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
import json
import subprocess
import urllib.request
import zipfile
import MySQLdb.cursors
import sys
from flask_mysqldb import MySQL
import mysql.connector
from werkzeug.utils import secure_filename
import pyunpack
import os
import urllib.request

from fileconversion import fileconversion1
from get_links import *
from linkedIn_main import*
from final_model import*

# BERT
MAX_LEN = 512
DEVICE = torch.device("cpu")
MODEL_PATH = 'bert-base-uncased'
STATE_DICT = torch.load(
    'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\model_e10.tar', map_location=DEVICE)
TOKENIZER = BertTokenizerFast.from_pretrained(MODEL_PATH, lowercase=True)
#TOKENIZER = Tokenizer(num_words=20000)  # SIMPLE
MODEL = BertForTokenClassification.from_pretrained(
    MODEL_PATH, state_dict=STATE_DICT['model_state_dict'], num_labels=12)
print('Model Loaded!')

tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
             'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']

# flask


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg',
                         'jpeg', 'docx', 'doc', 'rtf', 'odt', 'html', 'txt', 'zip'])


# functions
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binarydata = file.read()
    return binarydata


def convertBinaryToFile(binarydata, filename):
    with open(filename, 'wb') as file:
        file.write(binarydata)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# main-app
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
ZIPPED = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\zip"
app.config['ZIPPED'] = ZIPPED
EXTRACTED = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\extracted"
app.config['EXTRACTED'] = EXTRACTED

UPLOAD_FOLDER = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# routes
@app.route('/', methods=["POST", "GET"])
def login():
    return render_template('loginpage.html')


@app.route('/signup', methods=["POST", "GET"])
def signup():
    return render_template('signup.html')

@app.route('/verify', methods=["POST", "GET"])
def verify():
    table_pass=[]
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        email=request.form.get("emailid")
        password=request.form.get("pass")
        verify = cur.execute("Select password from login WHERE emailid= %s ", (email,))
        if verify > 0:
            row = cur.fetchall()
            for dict in row:
                table_pass.append(list(dict.values()))
            print(table_pass)
            print(str(table_pass[0][0]))
            print(password)

            if (str(password) == str(table_pass[0][0])) :
                print("in if")
                return render_template('Homepage.html')
            else:
                return redirect('/')

    else:
        return redirect('/')
    mysql.connection.commit()
    cur.close()


@app.route('/user', methods=["POST", "GET"])
def candiate():

        cur = mysql.connection.cursor()
        if request.method == 'POST':
                email = request.form.get("emailid")
                passw = request.form.get("pass")
                print(email)
                print(passw)

                cur.execute("INSERT INTO login(emailid,password) VALUES (%s, %s)",(email, passw,))
                mysql.connection.commit()
                cur.close()
                return redirect('/')









@app.route('/home', methods=["POST", "GET"])
def hello():
    return render_template('Homepage.html')


@app.route('/upload2', methods=["POST", "GET"])
def upload2():
    return render_template('upload2.html')


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    print('upload running')
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
        val = 1

       # enumerate(list)

        for file in files:
            print('files')

            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print(file.filename)
                name = ((file.filename).rsplit('.'))[1]
                if (name == 'zip'):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['ZIPPED'], filename))
                    zip_ref = zipfile.ZipFile(os.path.join(
                        app.config['ZIPPED'], filename), 'r')
                    zip_ref.extractall(app.config['EXTRACTED'])
                    dir_list = os.listdir(app.config['EXTRACTED'])
                    print(dir_list)
                    for i in dir_list:
                        original = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\extracted\\" + str(i)
                        x = original.rindex("\\")
                        y = original.rindex(".")
                        num = str(val)
                        val = val + 1
                        path = original[:x + 1] + "resume" + num + original[y:]
                        filerename = "resume" + num + original[y:]
                        os.rename(original, path)
                        # binary = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\"+filename
                        binartfile = convertToBinary(path)
                        # moving on to final folder
                        cur.execute("INSERT INTO deepbluecomp_table(files_path,binaryfiles_path) VALUES (%s, %s)",
                                    (filerename, binartfile))
                        print("------")
                        print(path, num)
                        text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion1(
                            path, num)
                        linkdedln, github, others = get_links(link)

                        cur.execute(
                            "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                            (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))
                        # model eval

                        # model(text)

                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for file_name in dir_list:
                        source = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\extracted\\" + file_name
                        destination = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\files\\" + file_name
                        shutil.move(source, destination)
                elif(name=='rar'):
                    filename = secure_filename(file.filename)
                    print(type(filename))
                    file.save(os.path.join(app.config['ZIPPED'], filename))

                    #zip_ref = zipfile.ZipFile(os.path.join(app.config['ZIPPED'], filename), 'r')
                    rarpath = pyunpack.Archive(os.path.join(app.config['ZIPPED'],filename))
                    rarpath.extractall(app.config['EXTRACTED'])

                    dir_list = os.listdir(app.config['EXTRACTED'])
                    print(dir_list)
                    for i in dir_list:
                        original = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\extracted\\" + str(i)
                        x = original.rindex("\\")
                        y = original.rindex(".")
                        num = str(val)
                        val = val + 1
                        path = original[:x + 1] + "resume" + num + original[y:]
                        filerename = "resume" + num + original[y:]
                        os.rename(original, path)

                        binartfile = convertToBinary(path)

                        cur.execute("INSERT INTO deepbluecomp_table(files_path,binaryfiles_path) VALUES (%s, %s)",
                                    (filerename, binartfile))
                        print("------")
                        text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion(
                            path, num)
                        linkdedln, github, others = get_links(link)

                        cur.execute(
                            "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                            (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))
                        # moving on to final folder
                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for file_name in dir_list:
                        source = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\extracted\\" + file_name
                        destination = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\" + file_name
                        shutil.move(source, destination)

                else:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    # inserting path to save the file *********************************************************
                    binary = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\files\\" + filename
                    #file1 = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\2021-12-08.png"
                    x = binary.rindex("\\")
                    y = binary.rindex(".")

                    num = str(val)
                    val = val+1

                    path = binary[:x + 1] + "resume" + num + binary[y:]
                    filerename = "resume" + num + binary[y:]
                    os.rename(binary, path)
                    #binary = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\"+filename
                    binartfile = convertToBinary(path)

                    cur.execute(
                        "INSERT INTO deepbluecomp_table(files_path,binaryfiles_path) VALUES (%s, %s)", (filerename, binartfile))
                    print(path)
                    print(num)
                    text2, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion1(
                        path, num)
                    linkdedln, github, others = get_links(link)

                    cur.execute(
                        "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                        (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))
                    print("------MODELS--------")
                    both_model(MODEL,TOKENIZER,DEVICE,text1)
                    
                    #proc = subprocess.Popen('python author_script.py {}{} -p n -s n -m num'.format(UPLOAD_FOLDER, file.filename), shell=True,stdout=subprocess.PIPE)

    mysql.connection.commit()
    # print(file)
    cur.close()
    flash('File(s) successfully uploaded')
    # return redirect('/upload')
    return render_template('table2.html')


@app.route("/delete")
def delete():
    dirzip_list = os.listdir(app.config['ZIPPED'])

    for zipfileli in dirzip_list:
        os.remove(
            "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\zip\\" + zipfileli)

    dirrar_list = os.listdir(app.config['EXTRACTED'])

    for rarfileli in dirrar_list:
        os.remove("C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\files\\" + rarfileli)        


    folder = "C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\static\\files"
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
    table_li = []

    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM list')
    # name,education,skills,experience,email
    print(result)
    if result > 0:
        row = cur.fetchall()
        print(row)
        for dict in row:
            table_li.append(list(dict.values()))
        print(table_li)

    return render_template('table2.html', row=table_li)

@app.route('/compare', methods=["POST", "GET"])
def compare():
    table_data=[]
    if request.method == "POST":
        candiatecomparelist = request.form.getlist('check')
        cur=mysql.connection.cursor()
        for i in candiatecomparelist:
            compresult=cur.execute("Select linked_link,github_link,extra_link from datastore WHERE sr= %s ",(int(i),))
            if compresult>0:
                row=cur.fetchall()
                for dict in row:
                    table_data.append(list(dict.values()))
                print(table_data)


    return render_template('statistics.html', cont=table_data)



if __name__ == "__main__":
    app.run(debug=True)

# app.run(debug=True)
# scrape_link = ''
# linkedien_scrape(scrape_link)
