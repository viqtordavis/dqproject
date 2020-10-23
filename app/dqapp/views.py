from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from . import dq_func
import json
import pandas as pd
import io
from .models import Sourcedb,Connections,Connectiondetails,Dqrules,Dqcheck,Dqcheckdetails,DqcheckRunBatch
from .forms import NewconnectionFormMysql,NewconnectionFormOracle,NewconnectionFormPostgres,NewdqcheckForm, RundqcheckForm
from .dqrunbatch import rundqchecks
from django.contrib.auth.models import User,auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .data_source import DataSource
from django.db import IntegrityError
import pandas_profiling as pp
import numpy as np



def home(request):
    return render(request,'index.html')


class newconnection(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    # raise_exception = False

    def get(self, request):
        global dblist
        dblist = Sourcedb.objects.all()
        return render(request,"newconnection.html",{'dblist' : dblist})

class newdqcheck(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def get(self, request):
        connectionlist = []
    
        Choices = Connections.objects.all()
        for choice in Choices:
            context={}
            context['id'] = choice.id
            context['connectionname'] =choice.connectionname
            connectionlist.append(context)
            print(context)
            print(connectionlist)
        return render(request,'adddqcheck.html',{'connectionlist':connectionlist})

class adddqcheck(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def post(self, request):
        dqcheckname = request.POST['dqcheckname']
        connection = request.POST['id_connections']
        tablename = request.POST['tables']
        columnname = request.POST.getlist('column')
        dqrule = request.POST.getlist('dqrule')
        optionvalues = request.POST.getlist('optvalues')

        try:
            dqcheck = Dqcheck.objects.create(dqcheckname=dqcheckname,connection=Connections.objects.get(id=connection),tablename=tablename)
            dqcheck.save()
        except IntegrityError as e:
            messages.success(request,'IntegrityError : There is a check already available with same name')
            return redirect('newdqcheck')

        for i in range(len(columnname)):
            dqcheckdetails = Dqcheckdetails.objects.create(dqcheck=Dqcheck.objects.get(dqcheckname=dqcheckname),tablename=tablename,columnname=columnname[i],dqrule=Dqrules.objects.get(dqrulename=dqrule[i]),optionvalues=optionvalues[i])
            dqcheckdetails.save()

            messages.info(request,'DataQuality Check Created! Go To Run DQ Checks to run the check.')
            return redirect('newdqcheck')
        
    def get(self, request):
        return render(request,'adddqcheck.html')

class rundqcheck(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def post(self, request):
        
        print(request.POST)
        dqcheck = request.POST['dqcheck']
        
        print(type(dqcheck))
        print("dqcheck is {}".format(dqcheck))

        runningcnt = DqcheckRunBatch.objects.filter(runstatus="Running",dqcheck=Dqcheck.objects.get(id=dqcheck)).count()

        print(runningcnt)

        if runningcnt == 0:
            dqcheckRunBatch = DqcheckRunBatch.objects.create(runstatus="Running",dqcheck=Dqcheck.objects.get(id=dqcheck),runstarttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            dqcheckRunBatch.save()
            print('runnig rundqchecks')
            dbname = rundqchecks(dqcheck,dqcheckRunBatch.id)
            print(dbname)
            return HttpResponse('')
        else:
            messages.info(request,'One DataQuality job is already running for this check. Please wait till it has finished.')
            return HttpResponse('')
       
        #messages.info(request,'Wait for run to complete')
        #return redirect('rundqcheck')
        #return render(request,'rundqcheck.html')
        

    def get(self, request):
        dqchecklist = []
        Choices = Dqcheck.objects.all()
    
        for choice in Choices:
            context = {}
            context['id']=choice.id
            context['dqcheckname']=choice.dqcheckname
            dqchecklist.append(context)
        print(dqchecklist)
        return render(request,'rundqcheckajax.html',{'dqchecklist':dqchecklist})

class addconnection(LoginRequiredMixin, View):
        login_url = '/accounts/login'
        redirect_field_name = 'next'
       
        def get(self, request):
            connectiontype = request.GET.get('connection')
            print(connectiontype)
            global selecteddbid
            selecteddbid = request.GET.get('selecteddb')
            print(selecteddbid)
            selecteddb=str(Sourcedb.objects.get(id=selecteddbid))
            print(selecteddb)
            if connectiontype is None:
                if selecteddbid is None:
                    return render(request,"newconnection.html",{'dblist' : dblist})
                elif selecteddbid == '1':
                    form_sql = NewconnectionFormMysql()
                    return render(request,'newform.html',{'form':form_sql})
                elif selecteddbid == '2':
                    form_sql = NewconnectionFormOracle()
                    return render(request,'newform.html',{'form':form_sql})
                elif selecteddbid == '5':
                    form_sql = NewconnectionFormPostgres()
                    return render(request,'newform.html',{'form':form_sql})
            elif connectiontype == 'Test Connection':
 
                    username = request.GET.get('username',"")
                    password = request.GET.get('password',"")
                    hostname = request.GET.get('hostname',"")
                    port = request.GET.get('port',"")
                    dbname = request.GET.get('dbname',"")
                    datasource = DataSource(selecteddb,username,password,hostname,port,dbname)
                    print(datasource)
                    connectionstatus = datasource.checkconnection()
                    print(connectionstatus)
                    # if connectionstatus is not None:
                    if  'pyodbc.Connection object at' in connectionstatus:
                        return HttpResponse("Connection Successful")
                    else:
                        val = connectionstatus
                        return HttpResponse("Connection Unsuccessful\n: {}".format(val) )
        def post(self, request):
                connectiontype = request.POST.get('connection')
                dblist = Sourcedb.objects.all()
                connname = request.POST['connectionname']
                schemaname = request.POST['schemaname']
                username = request.POST['username']
                password = request.POST['password']
                hostname = request.POST['hostname']
                port = request.POST['port']
                selecteddb=str(Sourcedb.objects.get(id=selecteddbid))
                if selecteddb == 'mysql':
                    dbname = request.POST['dbname']
                elif selecteddb == 'oracle':
                    dbname = ""
                elif selecteddb == 'postgres':
                    dbname = ""
                if connectiontype == 'Add Connection':

                    try:
                        connection = Connections.objects.create(connectionname=connname,sourcedb_id=selecteddbid)
                        connection.save()

                    except IntegrityError as e:
                        messages.success(request,'IntegrityError : There is a connection already available with same name')
                        return render(request,"newconnection.html",{'dblist' : dblist})

                    connectiondetail = Connectiondetails.objects.create(connection=Connections.objects.get(connectionname=connname),username=username,password=password,hostname=hostname,port=port,databasename=dbname,schemaname=schemaname)
                    connectiondetail.save()
                    
                    messages.success(request,'Connection Created')
                    return render(request,"newconnection.html",{'dblist' : dblist})
                    


def loadtables(request):
    connectionid = request.GET.get('connectionid')
    print(connectionid)

    tablelist = dq_func.getTablelist(connectionid)
    print(tablelist[0])
    
    return render(request,'loadtableslist.html',{'tablelist':tablelist})

def loadcolumnNrules(request):
    connectionid = request.GET.get('connectionid')
    tablename = request.GET.get('tablename')
    print(tablename)
    print(connectionid)

    columnlist = dq_func.getColumnlist(connectionid,tablename)

    dqrulelist = []
    DQrules = Dqrules.objects.all()
    for Dqrule in DQrules:
        dqrulelist.append(Dqrule.dqrulename)

    print(columnlist[0])
    
    return render(request,'loadColumnsAndDqRules.html',{'columnlist':columnlist,'dqrulelist':dqrulelist})

def loadbatchrun(request):
    dqcheckid = request.GET.get('dqcheckid')
    
    batchrunlist = []
    Choices = DqcheckRunBatch.objects.filter(dqcheck=dqcheckid).order_by('-id')
    
    for choice in Choices:
        context = {}
        context['id']=choice.id
        context['runstarttime']=choice.runstarttime
        context['runendtime']=choice.runendtime
        context['runstatus']=choice.runstatus
        batchrunlist.append(context)
        
    
    return render(request,'loadbatchrun.html',{'batchrunlist':batchrunlist})

# def fileupload(request):

#     return render(request,'dqcheckupload.html')

class fileupload(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    def get(self, request):
        return render(request,'dqcheckupload.html')
    
def runfileprofile(request):

    
    print(request.FILES, request.POST)
    #filedata = request.POST.get('dqcheckfile')
    filedata = request.FILES.get('file')
    #print(filedata)
    delimer = request.POST['delimiter']
    # filehead = request.POST.get('filehead', False)
    # filetrail = request.POST.get('filetrail', False)
    filehead = request.POST['filehead']
    filetrail = request.POST['filetrail']

    

    #print(filedata)
    print(delimer)
    print(filehead)
    print(filetrail)

    

    if delimer == 'comma':
        separator = ','
    elif delimer == 'pipe':
        separator = '|'
    elif delimer == 'tab':
        separator = '\t'
    else:
        separator = ','
    
    # filedataframe = pd.read_csv(io.StringIO(filedata),encoding='utf-8')
    filedataframe = pd.read_csv(filedata,sep=separator)
    print(filedataframe)
    profile = pp.ProfileReport(filedataframe)

    #print(profile)

    return HttpResponse(profile.to_html())

        
    

# def dqcheckupload(request):
    
    
#     if request.method == "POST":
#         uploaded_File = request.FILES['dqcheckfile']
#         fs = FileSystemStorage()
#         fs.save(uploaded_File.name,uploaded_File)
#         filename = uploaded_File.name
#         file = './fileuploads/' + filename
#         upload = dq_func.dq_check_upload(file)
    
#         if upload:
#             file = filename + ' uploaded successfully'
#             messages.info(request,file)
#             return redirect('fileupload')
#         else:
#             file = filename + ' not uploaded successfully'
#             messages.info(request,file)
#             return redirect('fileupload')
#     else:
#         return render(request,'dqcheckupload.html')