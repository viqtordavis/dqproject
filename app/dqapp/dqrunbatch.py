from .models import Sourcedb,Connections,Connectiondetails,Dqrules,Dqcheck,Dqcheckdetails,DqcheckRunBatch,DqcheckRunFact
from .data_source import DataSource
import pandas as pd
from .dqrulecalc import calcnullcnt,calctotalrowcnt,calcvalidvaluescnt
from datetime import datetime
import re


def rundqchecks(dqcheck,batchrunid):

    connectionid=Dqcheck.objects.get(id=dqcheck)
    connectiondetails=Connectiondetails.objects.get(connection_id=connectionid.connection_id)
    sourcedbid=Connections.objects.get(id=connectionid.connection_id)
    sourcedb=Sourcedb.objects.get(id=sourcedbid.sourcedb_id)

    datasource = DataSource(sourcedb.dbname,connectiondetails.username,connectiondetails.password,connectiondetails.hostname,connectiondetails.port,connectiondetails.databasename)

    connection = datasource.getconnection()

    dqcheckdetails = Dqcheckdetails.objects.filter(dqcheck_id=dqcheck)

    #print('no of columns {}'.format(len(dqcheckdetails)))
    
    if len(dqcheckdetails) == 1:
        columns = Dqcheckdetails.objects.get(dqcheck_id=dqcheck)
        #print(columns.columnname)
        sql_query = "SELECT {}  FROM {} ".format(columns.columnname,connectionid.tablename)
        columnResult = pd.read_sql(sql_query, connection)
        #print(columnResult.count())
    else:
        totalcolumns = len(dqcheckdetails)
        i=1
        columnname=''
        for check in dqcheckdetails:
            if i <= totalcolumns - 1:
                columnname = columnname + check.columnname + ','
            else:
                columnname = columnname + check.columnname
            
            i=i+1
        
        sql_query = "SELECT {}  FROM {} ".format(columnname,connectionid.tablename)
        columnResult = pd.read_sql(sql_query, connection)
        #print(columnResult.count())

    totalrowcnt = len(columnResult.index)
    print(totalrowcnt)

    print('inside rundqcheck')

    for check in dqcheckdetails:
        if check.dqrule_id == 1:
            
            #nullcnt = calcnullcnt(connection,check.columnname,check.tablename)
            nullcnt = columnResult[check.columnname].isna().sum()
            print(nullcnt)

            #totalrowcnt = calctotalrowcnt(connection,check.tablename)

            insertrow = DqcheckRunFact.objects.create(dqcheckdetailid=Dqcheckdetails.objects.get(id=check.id),measuredcount=nullcnt,totalcount=totalrowcnt,runbatchid=DqcheckRunBatch.objects.get(id=batchrunid))
            insertrow.save()

        elif check.dqrule_id == 2:
            print('inside valid values')
            #vvcnt = calcvalidvaluescnt(connection,check.columnname,check.tablename,check.optionvalues)
            optionlist = []
            
            optionvalues = check.optionvalues

            for validvalue in optionvalues.split(','):
                optionlist.append(validvalue)

            #optionlist.append(check.optionvalues)

            print(optionlist)

            vvcnt = columnResult[check.columnname][columnResult[check.columnname].isin(optionlist)].count() 
            print(vvcnt)

            #totalrowcnt = calctotalrowcnt(connection,check.tablename)

            insertrow = DqcheckRunFact.objects.create(dqcheckdetailid=Dqcheckdetails.objects.get(id=check.id),measuredcount=vvcnt,totalcount=totalrowcnt,runbatchid=DqcheckRunBatch.objects.get(id=batchrunid))
            insertrow.save()
            
        elif check.dqrule_id == 4:
            print('inside pattern check')
            #vvcnt = calcvalidvaluescnt(connection,check.columnname,check.tablename,check.optionvalues)

            pmcnt = 0
            print(check.optionvalues)

            optionvalues = check.optionvalues

            for pattern in optionvalues.split(','):
                expstr=''


                #patternlist = list(pattern)
                j=0
                for i in range(len(pattern)):

                    if j == 0:

                        if pattern[i] == '9':
                            expstr=expstr + '\d'
                        elif pattern[i] == 'A':
                            expstr=expstr + '[A-Z]'
                        elif pattern[i] == 'a':
                            expstr=expstr + '[a-z]'
                        elif pattern[i] == '"':
                            expstr=expstr + pattern[pattern.find('"')+1:pattern.rfind('"')]
                            j = pattern.rfind('"')
                            #print(j)
                        else:
                            expstr=expstr + '\\' + pattern[i]
                    else:

                        if i <= j:
                            continue
                        else:
                            if pattern[i] == '9':
                                expstr=expstr + '\d'
                            elif pattern[i] == 'A':
                                expstr=expstr + '[A-Z]'
                            elif pattern[i] == 'a':
                                expstr=expstr + '[a-z]'
                            elif pattern[i] == '"':
                                expstr=expstr + pattern[pattern.find('"')+1:pattern.rfind('"')]
                                j = pattern.rfind('"')
                                #print(j)
                            else:
                                expstr=expstr + '\\' + pattern[i]
                expstr = expstr + '$'
                print(expstr) 
                pmcnt = pmcnt + columnResult[check.columnname][columnResult[check.columnname].str.match(expstr) == True].count()
                print('pmcnt > ', pmcnt)

            #optionlist = []
            #optionlist.append(check.optionvalues)
            #print(optionlist)

            #vvcnt = columnResult[check.columnname][columnResult[check.columnname].isin(optionlist)].count() 
            #print(vvcnt)

            #totalrowcnt = calctotalrowcnt(connection,check.tablename)

            insertrow = DqcheckRunFact.objects.create(dqcheckdetailid=Dqcheckdetails.objects.get(id=check.id),measuredcount=pmcnt,totalcount=totalrowcnt,runbatchid=DqcheckRunBatch.objects.get(id=batchrunid))
            insertrow.save()

        else:
            print("error")
    
    batchrunrec = DqcheckRunBatch.objects.get(id=batchrunid)
    batchrunrec.runstatus = "Completed"
    batchrunrec.runendtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    batchrunrec.save()
    
        
    



         
        
    
        
    

