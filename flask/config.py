import torch

# spacy
# spacy_700_path = 'C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\models\\new'
# spacy_skills_path = 'models\\Models-Seprate-700\\SKILL'
# spacy_edu_path = 'models\\Models-Seprate-700\\EDU'
# spacy_exp_path = 'models\\Models-Seprate-700\\EXP'

# spacy_m2 = ""
# summary_model = ""


# # BERT
# # BERT
# MAX_LEN = 500 #512
# DEVICE = torch.device("cpu")
# MODEL_PATH = 'bert-base-uncased'
# bert_dict_path = "/home/aiworkstation2/Music/ser/DeepBlue/flask/models/model_e10.tar"


# #flask
# ZIPPED = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\zip"
# EXTRACTED = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\extracted"
# UPLOAD_FOLDER = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files"

# f2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files\\"
# e2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\extracted\\"
# z2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files\\zip\\"
# index = "\\"
driver_path = ""


#Om

#BERT
# MAX_LEN = 500 #512
# DEVICE = torch.device("cpu")
# MODEL_PATH = 'bert-base-uncased'
summary_model = '/Users/cosmos/Documents/DP-ref/Summary-100'
bert_dict_path = "/home/aiworkstation2/Music/ser/DeepBlue/flask/models/model_e10.tar"
spacy_700_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/new'
spacy_skills_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/SKILL'
spacy_edu_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/EDU'
spacy_exp_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/EXP'

f2 = 'static/files/'
e2 = 'static/zip/extracted/'
z2 = 'static/zip/'

ZIPPED = 'static/zip/' 
EXTRACTED = 'static/zip/extracted'
UPLOAD_FOLDER = 'static/files/' 
index = "/"

driver_path = "/Users/cosmos/chromedriver"



# if docker == 0:
#     os.system("docker run -d -p 9998:9998 logicalspark/docker-tikaserver")
#     docker = docker + 1
# else:
#     print("Docker already running")