from .models import Sourcedb,Connections,Connectiondetails,Dqrules,Dqcheck,Dqcheckdetails,DqcheckRunBatch
from .data_source import DataSource
import pandas as pd


def calcnullcnt(connection,column_name,table_name):

    sql_query = "SELECT count(1) as null_count FROM {} where {} is null ".format(table_name,column_name)

    columnResult = pd.read_sql(sql_query, connection)

    for index,row in columnResult.iterrows():
        return row.null_count


def calctotalrowcnt(connection,table_name):

    sql_query = "SELECT count(1) as total_count FROM {} ".format(table_name)

    columnResult = pd.read_sql(sql_query, connection)

    for index,row in columnResult.iterrows():
        return row.total_count
    
def calcvalidvaluescnt(connection,column_name,table_name,valid_value):

    sql_query = "SELECT count(1) as vv_count FROM {} where {} in ({})".format(table_name,column_name,valid_value)

    columnResult = pd.read_sql(sql_query, connection)

    for index,row in columnResult.iterrows():
        return row.vv_count
