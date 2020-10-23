from django.shortcuts import render, HttpResponse
from dqapp.models import Sourcedb,Connections,Connectiondetails,Dqrules,Dqcheck,Dqcheckdetails,DqcheckRunBatch,DqcheckRunFact
from .serializers import DqcheckRunFactSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from dqapp.data_source import DataSource
import pandas as pd
import pandas_profiling as pp
# Create your views here.


def dqcharts(request,id):
    
    return render(request,'charts.html',{'id':id})

def quickprofile(request,tablename):
    data=tablename.split('|')

    connectionid=int(data[0])
    tablename=data[1]

    connectiondetails=Connectiondetails.objects.get(connection_id=connectionid)
    sourcedbid=Connections.objects.get(id=connectionid)
    sourcedb=Sourcedb.objects.get(id=sourcedbid.sourcedb_id)

    datasource = DataSource(sourcedb.dbname,connectiondetails.username,connectiondetails.password,connectiondetails.hostname,connectiondetails.port,connectiondetails.databasename)

    connection = datasource.getconnection()

    sql_query = "SELECT *  FROM {} ".format(tablename)
    tabledf = pd.read_sql(sql_query, connection)

    profile = pp.ProfileReport(tabledf)
    

    return HttpResponse(profile.to_html())

def apichartsdata(request):
    
    id = request.GET.get('runbatchid')
    runfacts = DqcheckRunFact.objects.filter(runbatchid=DqcheckRunBatch.objects.get(id=id))

    nullchkcollist = []
    nullchkmeasuredcntlist = []
    validvalcollist = []
    validvalmeasuredcntlist = []
    patterncollist = []
    patternmeasuredcntlist = []
    nctotalcnt=0
    vvtotalcnt=0
    patterntotalcnt=0

    
    for dqcheckrunfact in dqcheckrunfacts:
        #context = {}
        print('checkdetailid', dqcheckrunfact.dqcheckdetailid_id)
        

        dqcheckdetail = Dqcheckdetails.objects.get(id=dqcheckrunfact.dqcheckdetailid_id)

        print('ruleid', dqcheckdetail.dqrule_id)

        dqrule = Dqrules.objects.get(id=dqcheckdetail.dqrule_id)
        if dqrule.dqrulename == "Null_Check":
            nullchkcollist.append(dqcheckdetail.columnname)
            nullchkmeasuredcntlist.append(dqcheckrunfact.measuredcount)
            nctotalcnt = dqcheckrunfact.totalcount
        
        elif dqrule.dqrulename == "Valid_Values":
            validvalcollist.append(dqcheckdetail.columnname)
            validvalmeasuredcntlist.append(dqcheckrunfact.measuredcount)
            vvtotalcnt = dqcheckrunfact.totalcount

        elif dqrule.dqrulename == "Pattern_Check":
            patterncollist.append(dqcheckdetail.columnname)
            patternmeasuredcntlist.append(dqcheckrunfact.measuredcount)
            patterntotalcnt = dqcheckrunfact.totalcount

        else:
            print("error")

        #context['measuredcount']=dqcheckrunfact.measuredcount
        #context['totalcount']=dqcheckrunfact.totalcount
        #context['minvalue']=dqcheckrunfact.minvalue
        #context['maxvalue']=dqcheckrunfact.maxvalue
        #context['avgvalue']=dqcheckrunfact.avgvalue
        #context['tablename']=dqcheckdetail.tablename
        #context['columnname']=dqcheckdetail.columnname
        #context['dqrulename']=dqrule.dqrulename

        #dqchecklist.append(context)
    print(nullchkcollist)
    print(nullchkmeasuredcntlist)

    data = {"Null_Check":{
        "labels":nullchkcollist,
        "measuredcount":nullchkmeasuredcntlist,
        "totalcount":nctotalcnt,
        "DqruleName" : "Null_Check" },
        "Valid_Values":{
        "labels":validvalcollist,
        "measuredcount":validvalmeasuredcntlist,
        "totalcount":vvtotalcnt,
        "DqruleName" : "Valid_Values" },
        "Pattern_Check":{
        "labels":patterncollist,
        "measuredcount":patternmeasuredcntlist,
        "totalcount":patterntotalcnt,
        "DqruleName" : "Pattern_Check" },
    }
    return JsonResponse(data,safe=False)
    #serializer = DqcheckRunFactSerializer(dqcheckrunfact,many=True)
    #serializer = DqcheckRunFactSerializer(data=dqchecklist,many=True)
    #if serializer.is_valid():
        
       
        #return JsonResponse(serializer.data, safe=False)
        
    #else:
     #   print(serializer.errors)
      #  return JsonResponse({"error":"object not valid", "status":400})


