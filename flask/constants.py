from nltk.corpus import stopwords
from webscrape import *

o1={}
o2={}
o3={}
o4={}
docker = 0

#FLASK
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg',
                         'jpeg', 'docx', 'doc', 'rtf', 'odt', 'html', 'txt', 'zip'])

databaseattribute = {'unknown': None, 'name': None, 'degree': None, 'skills': None, 'college_name': None,
                     'university': None, 'graduation_year': None, 'companies_worked_at': None, 'designation': None,
                     'years_of_experience': None, 'location': None,
                     'address': None, 'rewards_achievements': None, 'projects': None}
entities = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION', 'EMAIL ADDRESS', 'SKILLS',
            'YEARS OF EXPERIENCE', 'LOCATION', 'NAME']


#ML
tags_vals = ["UNKNOWN", "O", "Name", "Degree","Skills","College Name","Email Address","Designation","Companies worked at","Graduation Year","Years of Experience","Location"]
tag2idx = {t: i for i, t in enumerate(tags_vals)}
idx2tag = {i:t for i, t in enumerate(tags_vals)}


tagvalues_spacy = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION',
                   'EMAIL ADDRESS', 'SKILLS', 'YEARS OF EXPERIENCE', 'LOCATION', 'NAME  ', '']  # add more


words_stop = ["page 1 of 1","Resume", "page 1 of 2","page 1 of 3", "page 1 of 4",
                "page 2 of 2","page 3 of 3","page 4 of 4","page 2 of 3",
                "page 2 of 4","page 3 of 4","resume"]

NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

# Education (Upper Case Mandatory)
EDUCATION = [
            'BE', 'B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E',
            'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER = r'\d+'

# For finding date ranges
MONTHS_SHORT = r'''(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)
                   |(aug)|(sep)|(oct)|(nov)|(dec)'''
MONTHS_LONG = r'''(january)|(february)|(march)|(april)|(may)|(june)|(july)|
                   (august)|(september)|(october)|(november)|(december)'''
MONTH = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR = r'(((20|19)(\d{2})))'

STOPWORDS = set(stopwords.words('english'))

RESUME_SECTIONS_PROFESSIONAL = [
                    'experience',
                    'education',
                    'interests',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]

RESUME_SECTIONS_GRAD = [
                    'accomplishments',
                    'experience',
                    'education',
                    'interests',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]
