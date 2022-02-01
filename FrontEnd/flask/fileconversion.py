from docx2pdf import convert
import cv2
from fpdf import FPDF
from PIL import Image
import pdfkit
import os, os.path
import textract
import pytesseract
from flask import Flask, render_template, request, flash, redirect
from tika import parser
import tika
from preprocessing import*
from flask_mysqldb import MySQL, MySQLdb
import mysql
import mysql.connector
from preprocessing import *

def fileconversion(filename, y):
    eid=""
    phno=""

    fdate=""
    address=""
    # count=1
    #y = str(count)
    # filename = "C:\\Users\\Yash\\PycharmProjects\\firstprog\\resume.png"
    x = filename.rfind(".")
    extension = filename[x + 1:]
    if (extension == "docx"):
        converted = "resume" + y + ".pdf"
        name = "D:\\deepbluefiles\\" + converted
        convert(filename, name)
        raw = parser.from_file(name)
        text = raw['content']
        link=url(text)

        mailid=email(text)
        for i in mailid:
            eid=i +"  "
        if(eid is None):
            eid="null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno=j +"  "
        date=data_grabber(text)
        for k in date:
            fdate=str(k) +"  "
        human_name=get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address=ad + "  "
        pincode=pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext=remove_hexcode_rhc(text1)
        return (text1, link, eid, phno, fdate, human_name, address, pincode, ftext)

    elif (extension == "png" or extension == "jpg" or extension=="jpeg"):
        converted = "resume" + y + ".txt"
        name = "D:\\deepbluefiles\\" + converted
        file = open(name, "w")
        pdf = FPDF()
        pdf.add_page()
        fpdf = FPDF('L', 'cm', (500, 550))
        pdf.set_font("Arial", size=12)
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        img = cv2.imread(filename)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(pytesseract.image_to_string(img))

        file.write(pytesseract.image_to_string(img))

        cv2.imshow('Result', img)

        file.close()
        f = open(name, 'r')
        name1 = "D:\\deepbluefiles\\" + "resume" + y + ".pdf"
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='L')

        pdf.output(name1)
        raw = parser.from_file(name1)
        text = raw['content']
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)
        #cursor.execute("INSERT INTO datastore( data, link, emailid, phoneno, date, humaname, address, code, data_two) VALUES (%s, %s )",(text1, link, mailid, phone_number, date, human_name, add, pincode, ftext))
    #   cv2.waitKey(0)

    elif (extension == "txt"):
        converted = "resume" + y + ".pdf"
        name = "D:\\deepbluefiles\\" + converted
        pdf = FPDF()
        pdf.add_page()
        fpdf = FPDF('L', 'cm', (500, 550))
        pdf.set_font("Arial", size=11)
        f = open(filename, 'r')
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='L')

        pdf.output(name)
        raw = parser.from_file(name)
        text = raw['content']
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)
    elif (extension == "html"):
        converted = "resume" + y + ".pdf"
        name = "D:\\deepbluefiles\\" + converted
        with open(filename) as f:
            pdfkit.from_file(f, name)
        raw = parser.from_file(name)
        text = raw['content']
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = k + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)
    elif (extension == "rtf"):
        text = textract.process(filename)
        #print(text)
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)
    elif (extension == "odt"):
        text = textract.process(filename)
        #print(text)
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)

    elif (extension == "doc"):
        text = textract.process(filename)
        #print(text)
        link = url(text)
        for lin in link:
            scraplink = lin + "  "
        mailid = email(text)
        for i in mailid:
            eid = i + "  "
        if (eid is None):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, scraplink, eid, phno, fdate, human_name, address, pincode, ftext)

    elif(extension == "pdf"):
        raw = parser.from_file(filename)
        text = raw['content']
        link = url(text)

        mailid = email(text)
        for i in mailid:
            eid =" "+ i + " "
        if (eid ==" "):
            eid = "null"
        phone_number = get_phone_numbers(text)
        for j in phone_number:
            phno = j + "  "
        date = data_grabber(text)
        for k in date:
            fdate = str(k) + "  "
        human_name = get_human_names(text)
        add = address_grabber(text)
        for ad in add:
            address = ad + "  "
        pincode = pincode_grabber(text)
        text1 = pre_process1_rsw1(text)
        ftext = remove_hexcode_rhc(text1)
        return (text1, link, eid, phno, fdate, human_name, address, pincode, ftext)






