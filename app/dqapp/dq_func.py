import pyodbc
import os
import pandas as pd
##from sqlalchemy import create_engine
##import urllib
from .models import Connections,Connectiondetails


def dq_check_upload(file: str):

    
    
    file= pd.ExcelFile(file)

     ##dg = file.parse('Sheet1',encoding = "utf-8")

    df = file.parse('Sheet1')

    df['VALUES'] = df['VALUES'].fillna('')


    #params = urllib.parse.quote_plus('DRIVER={MySQL ODBC 8.0 Ansi Driver};UID=dq;Password=vqd2020;Server=localhost;Database=vqdq;Port=3306;')

    #engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

    cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};UID=dq;Password=vqd2020;Server=localhost;Database=vqdq;Port=3306;')

    cursor = cnxn.cursor()

    for index,row in df.iterrows():
                    
        cursor.execute("INSERT INTO vqdq.dq_check_details(table_name,column_name,dq_rule_id,dq_rule_values) \
                            values (?,?,(select dq_rule_id from vqdq.dq_rules where dq_rule_name = ?),?)", \
                            str(row['TABLE_NAME']).encode('ISO-8859-1'),str(row['COLUMN_NAME']).encode('ISO-8859-1'),str(row['DQ_RULE']).encode('ISO-8859-1'),\
                                str(row['VALUES']).encode('ISO-8859-1')
                            )
    cnxn.commit()
    cursor.close()
    cnxn.close()
    return True


# def getSourceDatabases():

#     src = []

#     cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};UID=dq;Password=vqd2020;Server=localhost;Database=vqdq;Port=3306;')
#     cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
#     cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
#     cnxn.setencoding(encoding='iso-8859-1')

#     tableResult = pd.read_sql("select db_name from vqdq.db_details;", cnxn) 
#     #cursor = cnxn.cursor()

#     #srcs = cursor.execute("select db_name from vqdq.db_details;")
#     #src = srcs.fetchall()

#     for index,row in tableResult.iterrows():
#         src.append(row['db_name'])
    
#     #cursor.close()
#     cnxn.close()
#     return src

def getTablelist(connectionid: str):

    src = []

    conn = Connectiondetails.objects.get(connection_id=connectionid)

    user = conn.username
    password = conn.password
    hostname = conn.hostname
    port = conn.port
    databasename = conn.databasename
    schemaname = conn.schemaname

    driver = 'DRIVER={MySQL ODBC 8.0 Ansi Driver}'
    connectstr = f'{driver};uid={user};Password={password};Server={hostname};Database={databasename};Port={port};'


    cnxn = pyodbc.connect(connectstr)
    cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
    cnxn.setencoding(encoding='iso-8859-1')

    sql_query = "SELECT table_name FROM information_schema.tables where table_schema='{}'".format(schemaname)

    tableResult = pd.read_sql(sql_query, cnxn) 

    for index,row in tableResult.iterrows():
        src.append(row.TABLE_NAME)
    
    cnxn.close()
    return src

def getColumnlist(connectionid: str,tablename: str):

    col = []

    conn = Connectiondetails.objects.get(connection_id=connectionid)

    user = conn.username
    password = conn.password
    hostname = conn.hostname
    port = conn.port
    databasename = conn.databasename
    schemaname = conn.schemaname

    driver = 'DRIVER={MySQL ODBC 8.0 Ansi Driver}'
    connectstr = f'{driver};uid={user};Password={password};Server={hostname};Database={databasename};Port={port};'


    cnxn = pyodbc.connect(connectstr)
    cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
    cnxn.setencoding(encoding='iso-8859-1')

    sql_query = "SELECT column_name FROM information_schema.columns where table_schema='{}' and table_name='{}'".format(schemaname,tablename)

    columnResult = pd.read_sql(sql_query, cnxn) 

    for index,row in columnResult.iterrows():
        col.append(row.COLUMN_NAME)
    
    cnxn.close()
    return col


    
# def checkconnection(request):

#     connname = request.POST['connectionname']
#     schemaname = request.POST['schemaname']
#     user = request.POST['username']
#     password = request.POST['password']
#     hostname = request.POST['hostname']
#     port = request.POST['port']
#     databasename = request.POST.get('dbname',"NA")
#     print(databasename)

#     driver = 'DRIVER={MySQL ODBC 8.0 Ansi Driver}'
#     connectstr = f'{driver};uid={user};Password={password};Server={hostname};Database={databasename};Port={port};'
#     print(connectstr)

#     try:
#         cnxn = pyodbc.connect(connectstr)

#     except pyodbc.Error as ex:
#         return None

#     if cnxn:
#         cnxn.close()
#         return cnxn
        