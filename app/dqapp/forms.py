from django import forms
from . models import Sourcedb, Connectiondetails, Connections, Dqcheck
from django.forms import ModelForm


class NewconnectionFormMysql(forms.Form):
    # dblist = []
    # Choices = Sourcedb.objects.all()
    # for Choice in Choices:
    #     tup=(Choice.id,Choice.dbname)
    #     dblist.append(tup)
    
    #sourcedb = forms.ChoiceField(choices=dblist,label='Select Source Database ',initial='')
    #sourcedb = forms.ModelChoiceField(required=True, widget=forms.Select, queryset=Sourcedb.objects.all())
    dbname = forms.CharField(label='Enter database name         ')
    schemaname = forms.CharField(label='Enter schema name       ')
    username = forms.CharField(label='Enter user name           ')
    password = forms.CharField(label='Enter password            ',widget=forms.PasswordInput)
    hostname = forms.CharField(label='Enter database hostname   ')
    port = forms.CharField(label='Enter database port           ')
    sid = forms.CharField(label='Enter database sid             ',required=False)
    connectionname = forms.CharField(label='Connection name to save')

class NewconnectionFormOracle(forms.Form):

    schemaname = forms.CharField(label='Enter schema name')
    username = forms.CharField(label='Enter user name')
    password = forms.CharField(label='Enter password ',widget=forms.PasswordInput)
    hostname = forms.CharField(label='Enter database hostname')
    port = forms.CharField(label='Enter database port')
    #sid = forms.CharField(label='Enter database sid',required=False)
    connectionname = forms.CharField(label='Connection name to save')

class NewconnectionFormPostgres(forms.Form):

    schemaname     = forms.CharField(label='Enter schema name')
    username       = forms.CharField(label='Enter user name  ')
    password       = forms.CharField(label='Enter password   ',widget=forms.PasswordInput)
    hostname       = forms.CharField(label='Enter database hostname')
    port           = forms.CharField(label='Enter database port')
    connectionname = forms.CharField(label='Connection name to save')

class NewdqcheckForm(forms.Form):
    
    connectionlist = [(0,'--------')]
    Choices = Connections.objects.all()
    for choice in Choices:
        tup = (choice.id,choice.connectionname)
        connectionlist.append(tup)
    
    connections = forms.ChoiceField(choices=connectionlist,label='Select Database Connection ')

class RundqcheckForm(forms.Form):
    dqchecklist = [(0,'--------')]
    Choices = Dqcheck.objects.all()

    for choice in Choices:
        tup = (choice.id,choice.dqcheckname)
        dqchecklist.append(tup)

    dqcheckname = forms.ChoiceField(choices=dqchecklist,label='Select Check ')
    


    
    



