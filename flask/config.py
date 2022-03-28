import torch

# spacy
spacy_700_path = 'C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\models\\new'
spacy_skills_path = 'models\\Models-Seprate-700\\SKILL'
spacy_edu_path = 'models\\Models-Seprate-700\\EDU'
spacy_exp_path = 'models\\Models-Seprate-700\\EXP'

spacy_m2 = ""
summary_model = ""


# BERT
# BERT
MAX_LEN = 500 #512
DEVICE = torch.device("cpu")
MODEL_PATH = 'bert-base-uncased'
bert_dict_path = "/home/aiworkstation2/Music/ser/DeepBlue/flask/models/model_e10.tar"


#flask
ZIPPED = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\zip"
EXTRACTED = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\extracted"
UPLOAD_FOLDER = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files"

f2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files\\"
e2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\extracted\\"
z2 = "C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\flask\\static\\files\\zip\\"
index = "\\"
driver_path = ""


#Om

# BERT
# MAX_LEN = 500 #512
# DEVICE = torch.device("cpu")
# MODEL_PATH = 'bert-base-uncased'
# summary_model = ''
# bert_dict_path = "/home/aiworkstation2/Music/ser/DeepBlue/flask/models/model_e10.tar"
# spacy_700_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/new'
# spacy_skills_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/SKILL'
# spacy_edu_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/EDU'
# spacy_exp_path = '/Users/cosmos/Desktop/DeepBlue/flask/models/Models-Seprate-700/EXP'

# f2 = '/Users/cosmos/Desktop/DeepBlue/flask/static/files/'
# e2 = '/Users/cosmos/Desktop/DeepBlue/flask/static/zip/extracted/'
# z2 = '/Users/cosmos/Desktop/DeepBlue/flask/static/zip/'

# ZIPPED = '/Users/cosmos/Desktop/DeepBlue/flask/static/zip/' 
# EXTRACTED = '/Users/cosmos/Desktop/DeepBlue/flask/static/zip/extracted'
# UPLOAD_FOLDER = '/Users/cosmos/Desktop/DeepBlue/flask/static/files/' 
# index = "/"

# driver_path = "/Users/cosmos/chromedriver"