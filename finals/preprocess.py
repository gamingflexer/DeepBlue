import tika
from tika import parser
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from date_extractor import extract_dates
import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import pyap



#defines
words_stop = ["page 1 of 1","Resume", "page 1 of 2","page 1 of 3", "page 1 of 4", 
                "page 2 of 2","page 3 of 3","page 4 of 4","page 2 of 3",
                "page 2 of 4","page 3 of 4","resume"]

extracted_dates = {}
person_list = []
person_names=person_list

stop_words = set(stopwords.words('english'))
stop_words = list(stop_words.union(words_stop))




##############################################################################################################################

#url function
def url_grabber(text0):
    url =["",""]
    for i in range(0,2):
        url[i] = re.search("(?P<url>https?://[^\s]+)", text).group("url")
        name = "text" + i
        name = text0.replace(url[0],"")
    return url

#get number
def no_grabbber(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers]

#email getter

def email_grabbber(text):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return emails

#dates grabber
def data_grabber(text):
    dates = extract_dates(text)
    return dates

#name grabber
def name_grabber(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
        
        
#names = name_grabber(text)
for person in person_list:
    person_split = person.split(" ")
    for name in person_split:
        if wordnet.synsets(name):
            if(name in person):
                person_names.remove(person)
                break

print(person_names)


#address
def address_grabber(text):
    addresses = pyap.parse(text, country='US')
    return addresses

#find pincode
def pincode_grabber(text):
    pincode =  r"[^\d][^a-zA-Z\d](\d{6})[^a-zA-Z\d]"
    pattern = re.compile(pincode)
    result = pattern.findall(text)
    if len(result)==0:
        return ' '
    return result[0]

#dob grabber
def dob_grabber(text, ents):
        dob = 'Not found'
        lines = [line.strip() for line in text.split('\n')]
        dob_pattern = r'((\d)?(\d)(th)?.((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)|(january)|(february)|(march)|(april)|(may)|(june)|(july)|(august)|(september)|(october)|(november)|(december)|(\d{2})).(\d{4}))'
        required = ''
        matches = ['dob', 'date of birth', 'birth date']
        flag = 0
        count = 0
        for lin in lines:
            
            if any(x in lin.lower().strip() for x in matches):
                required = lin.lower() +'\n'
                flag = 1
            if flag == 1:
                if len(lin.split()) < 1:continue
                required += lin.lower() + '\n'
                count +=1
            if count > 4:
                break        
        required = ' '.join(req for req in required.split())

        match = re.findall(dob_pattern, required)
        try:
            return match[0][0]
        except:
            return ''


##############################################################################################################################

#preprocessing 

def pre_process1(text):
    text = "".join(text.split('\n')) #remove whitespaces
    text = text.lower()
    
    #using re
    text=re.sub('http\S+\s*',' ',text)
    text=re.sub('RT|cc',' ',text)
    text=re.sub('#\S+',' ',text)
    text=re.sub('@\S+',' ',text)
    
    #for i in range (len(emails)): #removes emails
     #   text = text.replace(emails[i],"") 
    
    text = re.sub(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})','',text) #removes phone numbers
    text=re.sub(r'[^\x00-\x7f]',' ',text)
    text=re.sub('\s+',' ',text)
    text=re.sub("\n", " ",text)
    
    #remove uncessary stop words
    for i in range (len(words_stop)): #removes emails
        text = text.replace(words_stop[i],"") 
    
    return ''.join(text)



#remove stop words
def pre_process2(text):
    stop_words= set(stopwords.words("english"))
    word_tokens=word_tokenize(text)
    new_text= [word for word in word_tokens if word not in stopwords]
    return new_text

#remove puncutations
def pre_process3(text):
    translator=str.maketrans(",",string.punctuation)
    return text.translate(translator)


#remove hex code
def remove_hexcode(text):
    text = re.sub(r'[^\x00-\x7f]',r'', text) 
    return text
    

#Removes non-alphabetic characters:
def text_strip(column):
    for row in column:
        
        #ORDER OF REGEX IS VERY VERY IMPORTANT!!!!!!
        
        row=re.sub("(\\t)", ' ', str(row)).lower() #remove escape charecters
        row=re.sub("(\\r)", ' ', str(row)).lower() 
        row=re.sub("(\\n)", ' ', str(row)).lower()
        
        row=re.sub("(__+)", ' ', str(row)).lower()   #remove _ if it occors more than one time consecutively
        row=re.sub("(--+)", ' ', str(row)).lower()   #remove - if it occors more than one time consecutively
        row=re.sub("(~~+)", ' ', str(row)).lower()   #remove ~ if it occors more than one time consecutively
        row=re.sub("(\+\++)", ' ', str(row)).lower()   #remove + if it occors more than one time consecutively
        row=re.sub("(\.\.+)", ' ', str(row)).lower()   #remove . if it occors more than one time consecutively
        
        row=re.sub(r"[<>()|&©ø\[\]\'\",;?~*!]", ' ', str(row)).lower() #remove <>()|&©ø"',;?~*!
        
        row=re.sub("(mailto:)", ' ', str(row)).lower() #remove mailto:
        row=re.sub(r"(\\x9\d)", ' ', str(row)).lower() #remove \x9* in text
        row=re.sub("([iI][nN][cC]\d+)", 'INC_NUM', str(row)).lower() #replace INC nums to INC_NUM
        row=re.sub("([cC][mM]\d+)|([cC][hH][gG]\d+)", 'CM_NUM', str(row)).lower() #replace CM# and CHG# to CM_NUM
        
        
        row=re.sub("(\.\s+)", ' ', str(row)).lower() #remove full stop at end of words(not between)
        row=re.sub("(\-\s+)", ' ', str(row)).lower() #remove - at end of words(not between)
        row=re.sub("(\:\s+)", ' ', str(row)).lower() #remove : at end of words(not between)
        
        row=re.sub("(\s+.\s+)", ' ', str(row)).lower() #remove any single charecters hanging between 2 spaces
        
        #Replace any url as such https://abc.xyz.net/browse/sdf-5327 ====> abc.xyz.net
        try:
            url = re.search(r'((https*:\/*)([^\/\s]+))(.[^\s]+)', str(row))
            repl_url = url.group(3)
            row = re.sub(r'((https*:\/*)([^\/\s]+))(.[^\s]+)',repl_url, str(row))
        except:
            pass #there might be emails with no url in them
        

        
        row = re.sub("(\s+)",' ',str(row)).lower() #remove multiple spaces
        
        #Should always be last
        row=re.sub("(\s+.\s+)", ' ', str(row)).lower() #remove any single charecters hanging between 2 spaces

        yield row


