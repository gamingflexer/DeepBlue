def databasevalue(listofvalues):
    insertdata=""
    if(listofvalues=='Null'):
        return 'Null'
    else:
        for value in listofvalues:
            insertdata=insertdata+value +","

        return insertdata
