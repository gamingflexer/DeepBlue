from flask import *
import mysql
import app
import MySQLdb.cursors
import mysql.connector
from flask_mysqldb import MySQL, MySQLdb
from funcdatabse import databasevalue

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepblue'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'deepbluecomp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/', methods=["POST", "GET"])
def hello():
    cur = mysql.connection.cursor()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    dictionary = {'NAME': ['yash', 'anish', 'om', 'kunal', 'adwaith'], 'COMPANIES WORKED AT': ['MUMBAI', 'DELHI'],
                  'COLLEGE NAME': ['PCE', 'SVS']}
    databaseattribute = {'unknown': None, 'name': None, 'degree': None, 'skills': None, 'college_name': None,
                         'university': None, 'graduation_year': None, 'companies_worked_at': None, 'designation': None,
                         'years_of_experience': None, 'location': None,
                         'address': None, 'rewards_achievements': None, 'projects': None}
    entities = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION', 'EMAIL ADDRESS', 'SKILLS',
                'YEARS OF EXPERIENCE', 'LOCATION', 'NAME']

    for entity in entities:
        if entity in dictionary.keys():
            values = dictionary.get(entity)
            if (entity.replace(" ", "_").lower() in databaseattribute.keys()):
                databaseattribute.update({entity.replace(" ", "_").lower(): values})

    print(databaseattribute)
    for key, values in databaseattribute.items():
        if (databaseattribute[key] == None):
            databaseattribute[key] = 'Null'
    print(databaseattribute)


    cur.execute("INSERT INTO model(unknown,name,degree,skills,college_name,university,graduation_year,companies_worked_at,designation,years_of_experience,location,address,rewards_achievements,projects) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (databasevalue(databaseattribute.get('unknown')),databasevalue(databaseattribute.get('name')),databasevalue(databaseattribute.get('degree')),databasevalue(databaseattribute.get('skills')),databasevalue(databaseattribute.get('college_name')),databasevalue(databaseattribute.get('university')),databasevalue(databaseattribute.get('graduation_year')),databasevalue(databaseattribute.get('companies_worked_at')),databasevalue(databaseattribute.get('designation')),databasevalue(databaseattribute.get('years_of_experience')),databasevalue(databaseattribute.get('location')),databasevalue(databaseattribute.get('address')),databasevalue(databaseattribute.get('rewards_achievements')),databasevalue(databaseattribute.get('projects')),))
    mysql.connection.commit()
    cur.close()
    for key, values in databaseattribute.items():
        databaseattribute[key] = 'Null'
    print(databaseattribute)
    return render_template('Homepage.html')


if __name__ == "__main__":
    app.run(debug=True)
