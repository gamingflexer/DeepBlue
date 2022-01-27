import textract
#import pdfminer
import os

# text = textract.process('/Users/cosmos/Documents/ilovepdf_pages-to-jpg/yashresume_page-0001.jpg')
# print(text)

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
for page_layout in extract_pages("/Users/cosmos/Documents/yashresume.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())