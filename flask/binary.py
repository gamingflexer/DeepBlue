from ast import Return
from flask import Flask, render_template, request, flash, redirect
from flask import *
import os
import shutil
from flask_mysqldb import MySQL, MySQLdb
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import mysql
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch
import pyperclip
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
from keras.preprocessing.sequence import pad_sequences

from fileconversion import fileconversion1
from preprocessing import*
from get_links import *
from linkedIn_main import*
from final_model import*
from funcdatabse import databasevalue


# BERT
MAX_LEN = 500
DEVICE = torch.device("cpu")
MODEL_PATH = 'bert-base-uncased'
STATE_DICT = torch.load(
   '/home/aiworkstation2/Music/ser/DeepBlue/flask/models/model_e10.tar', map_location=DEVICE)
TOKENIZER = BertTokenizerFast.from_pretrained(MODEL_PATH, lowercase=True)
#TOKENIZER = Tokenizer(num_words=20000)  # SIMPLE
MODEL = BertForTokenClassification.from_pretrained(
   MODEL_PATH, state_dict=STATE_DICT['model_state_dict'], num_labels=12)
model = MODEL
MODEL.to(DEVICE);
print('\nModel Loaded!\n')
tags_vals = ["UNKNOWN", "O", "Name", "Degree","Skills","College Name","Email Address","Designation","Companies worked at","Graduation Year","Years of Experience","Location"]
tag2idx = {t: i for i, t in enumerate(tags_vals)}
idx2tag = {i:t for i, t in enumerate(tags_vals)}

tokenizer_bert_ner = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model_bert_ner = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
print('\n NER Model Loaded!\n')
# flask

o1={}
o2={}
o3={}
o4={}
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
ZIPPED = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/zip"
app.config['ZIPPED'] = ZIPPED
EXTRACTED = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/extracted"
app.config['EXTRACTED'] = EXTRACTED

UPLOAD_FOLDER = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
databaseattribute = {'unknown': None, 'name': None, 'degree': None, 'skills': None, 'college_name': None,
                         'university': None, 'graduation_year': None, 'companies_worked_at': None, 'designation': None,
                         'years_of_experience': None, 'location': None,
                         'address': None, 'rewards_achievements': None, 'projects': None}
entities = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION', 'EMAIL ADDRESS', 'SKILLS',
                'YEARS OF EXPERIENCE', 'LOCATION', 'NAME']
# routes

def process_resume2(text, tokenizer, max_len):
    tok = tokenizer.encode_plus(text, max_length=max_len, return_offsets_mapping=True)
    
    curr_sent = dict()
    
    padding_length = max_len - len(tok['input_ids'])
        
    curr_sent['input_ids'] = tok['input_ids'] + ([0] * padding_length)
    curr_sent['token_type_ids'] = tok['token_type_ids'] + ([0] * padding_length)
    curr_sent['attention_mask'] = tok['attention_mask'] + ([0] * padding_length)
    
    final_data = {
        'input_ids': torch.tensor(curr_sent['input_ids'], dtype=torch.long),
        'token_type_ids': torch.tensor(curr_sent['token_type_ids'], dtype=torch.long),
        'attention_mask': torch.tensor(curr_sent['attention_mask'], dtype=torch.long),
        'offset_mapping': tok['offset_mapping']
    }
    
    return final_data

def predict(model, tokenizer, idx2tag, tag2idx, device, test_resume):
    model.eval()
    data = process_resume2(test_resume, tokenizer, MAX_LEN)
    input_ids, input_mask = data['input_ids'].unsqueeze(0), data['attention_mask'].unsqueeze(0)
    labels = torch.tensor([1] * input_ids.size(0), dtype=torch.long).unsqueeze(0)
    with torch.no_grad():
        outputs = model(
            input_ids,
            token_type_ids=None,
            attention_mask=input_mask,
            labels=labels,
        )
        tmp_eval_loss, logits = outputs[:2]
    
    logits = logits.cpu().detach().numpy()
    label_ids = np.argmax(logits, axis=2)
    
    entities = []
    for label_id, offset in zip(label_ids[0], data['offset_mapping']):
        curr_id = idx2tag[label_id]
        curr_start = offset[0]
        curr_end = offset[1]
        if curr_id != 'O':
            if len(entities) > 0 and entities[-1]['entity'] == curr_id and curr_start - entities[-1]['end'] in [0, 1]:
                entities[-1]['end'] = curr_end
            else:
                entities.append({'entity': curr_id, 'start': curr_start, 'end':curr_end})
    for ent in entities:
        ent['text'] = test_resume[ent['start']:ent['end']]
    return entities

print('\nFlask Started!\n')

@app.route('/', methods=["POST", "GET"])
def login():
    return render_template('loginpage.html')


@app.route('/signup', methods=["POST", "GET"])
def signup():
    return render_template('signup.html')

@app.route('/verify', methods=["POST", "GET"])
def verify():
    table_pass=[]
    print("under verify")
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        email=request.form.get("emailid")
        # print(email)
        password=request.form.get("pass")
        # print(password)
        verify = cur.execute("Select password from login WHERE emailid= %s ", (email,))
        print('database')
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
                # print(email)
                # print(passw)

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
    print('\n upload running \n')
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
                        original = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/extracted/" + str(i)
                        x = original.rindex("/")
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
                        text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion1(
                            path, num)
                        linkdedln, github, others = get_links(link)

                        cur.execute(
                            "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                            (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))


                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for file_name in dir_list:
                        source = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/extracted/" + file_name
                        destination = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files/" + file_name
                        shutil.move(source, destination)
                elif(name=='rar'):
                    filename = secure_filename(file.filename)
                    print(type(filename))
                    file.save(os.path.join(app.config['ZIPPED'], filename))

                    #zip_ref = zipfile.ZipFile(os.path.join(app.config['ZIPPED'], filename), 'r')
                    rarpath = pyunpack.Archive(os.path.join(app.config['ZIPPED'],filename))
                    rarpath.extractall(app.config['EXTRACTED'])

                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for i in dir_list:
                        original = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/extracted/" + str(i)
                        x = original.rindex("/")
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
                        text, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion1(
                            path, num)
                        linkdedln, github, others = get_links(link)

                        cur.execute(
                            "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                            (text1, ftext, pincode, mailid, linkdedln, github, others, phone_number))
                        # moving on to final folder
                    dir_list = os.listdir(app.config['EXTRACTED'])
                    for file_name in dir_list:
                        source = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/extracted/" + file_name
                        destination = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files/" + file_name
                        shutil.move(source, destination)

                else:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    # inserting path to save the file *********************************************************
                    binary = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files/" + filename
                    #file1 = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\2021-12-08.png"
                    x = binary.rindex("/")
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
                    
                    text2, text1, link, mailid, phone_number, date, human_name, add, pincode, ftext = fileconversion1(
                        path, num)
                    linkdedln, github, others = get_links(link)
                    #add to database
                    cur.execute(
                        "INSERT INTO parse( extracted_text, cleaned_text,state, emails, linkedin_link, github_link,extra_link,phonenumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                        (text2, ftext, pincode, mailid, linkdedln, github, others, phone_number))

                    print("\n------MODELS--------\n")
                    print('------SPACY--------')
                    oo1 = spacy_700(text1)
                    oo2 = spacy_700(text2)

                    for entity in entities:
                        if entity in oo2.keys():
                            values = oo2.get(entity)
                            if (entity.replace(" ", "_").lower() in databaseattribute.keys()):
                                databaseattribute.update({entity.replace(" ", "_").lower(): values})

                    #print(databaseattribute)
                    for key, values in databaseattribute.items():
                        if (databaseattribute[key] == None):
                            databaseattribute[key] = 'Null'
                    


                    cur.execute("INSERT INTO model(unknown,name,degree,skills,college_name,university,graduation_year,companies_worked_at,designation,years_of_experience,location,address,rewards_achievements,projects) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (databasevalue(databaseattribute.get('unknown')),databasevalue(databaseattribute.get('name')),databasevalue(databaseattribute.get('degree')),databasevalue(databaseattribute.get('skills')),databasevalue(databaseattribute.get('college_name')),databasevalue(databaseattribute.get('university')),databasevalue(databaseattribute.get('graduation_year')),databasevalue(databaseattribute.get('companies_worked_at')),databasevalue(databaseattribute.get('designation')),databasevalue(databaseattribute.get('years_of_experience')),databasevalue(databaseattribute.get('location')),databasevalue(databaseattribute.get('address')),databasevalue(databaseattribute.get('rewards_achievements')),databasevalue(databaseattribute.get('projects')),))
                
                    for key, values in databaseattribute.items():
                        databaseattribute[key] = 'Null'
                   


                    
                    oo3 = spacy_700(ftext)
                    # oo2 = spacy_skills(text1)
                    # oo3 = spacy_edu(text1)
                    # oo4 = spacy_exp(text1)
                    # print(oo1)
                    print(oo2)
                    # print(oo3)
                    # print(oo4)
                    #entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text1)
                    #output_bert = clean_bert(entities1, tags_vals)
                    #print(output_bert)
                    #print("------BERT--------")
                    # entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text1)
                    # output_bert = clean_bert(entities1, tags_vals)
                    # print(output_bert)
                    print("------NAME--------")
                    name_extracted = ner(text2,model_bert_ner,tokenizer_bert_ner) #is a list
                    print(name_extracted)
                    
                    #Linkdien
                    # if linkdedln != None:
                    #     if mailid or pincode is not None: #add here
                    #         linkdien_data = linkedien_scrape(linkdedln[0])
                    #         print(linkdien_data)
                    
    mysql.connection.commit()
    cur.close()
    flash('File(s) successfully uploaded')
    # return redirect('/upload')
    return render_template('table2.html')


@app.route("/delete")
def delete():
    dirzip_list = os.listdir(app.config['ZIPPED'])

    for zipfileli in dirzip_list:
        os.remove(
            "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/zip/" + zipfileli)

    dirrar_list = os.listdir(app.config['EXTRACTED'])

    for rarfileli in dirrar_list:
        os.remove("/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files/" + rarfileli)        


    folder = "/home/aiworkstation2/Music/ser/DeepBlue/flask/static/files"
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
    if result > 0:
        row = cur.fetchall()
        for dict in row:
            table_li.append(list(dict.values()))

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

