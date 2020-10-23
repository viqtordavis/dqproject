from django.db import models

# Create your models here.

class Sourcedb(models.Model):
    dbname = models.CharField(max_length = 100)
    def __str__(self):
        return self.dbname



class Connections(models.Model):
    connectionname = models.CharField(max_length = 100,unique=True)
    sourcedb = models.ForeignKey('Sourcedb', on_delete=models.CASCADE)

class Connectiondetails(models.Model): 
    connection = models.ForeignKey('Connections', on_delete=models.CASCADE)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    hostname = models.CharField(max_length = 100)
    port = models.CharField(max_length = 10)
    databasename = models.CharField(max_length = 50)
    connectstring = models.CharField(max_length = 200,null=True,editable=True)
    schemaname = models.CharField(max_length = 50 ,null=True)

class Dqrules(models.Model):
    dqrulename = models.CharField(max_length = 100,unique=True)
    dqruledesc = models.TextField(blank=True,editable=True)

class Dqrulesql(models.Model):
    dqrule = models.ForeignKey('Dqrules',on_delete = models.CASCADE)
    sqlstmt = models.TextField()

class Dqcheck(models.Model):
    dqcheckname = models.CharField(max_length = 100,unique=True)
    connection = models.ForeignKey('Connections',on_delete=models.CASCADE)
    tablename = models.CharField(max_length = 100,null=True)

class Dqcheckdetails(models.Model):
    dqcheck = models.ForeignKey('Dqcheck',on_delete=models.CASCADE)
    tablename = models.CharField(max_length = 100)
    columnname = models.CharField(max_length = 100)
    dqrule = models.ForeignKey('Dqrules',on_delete=models.CASCADE)
    optionvalues = models.TextField() 

class DqcheckRunBatch(models.Model):
    dqcheck = models.ForeignKey('Dqcheck',on_delete=models.CASCADE)
    runstatus = models.CharField(max_length = 20,null=False)
    runstarttime = models.CharField(max_length=20,null=False)
    runendtime = models.CharField(max_length=20,null=True)


class DqcheckRunFactSample(models.Model):
    dqcheckdetailid = models.ForeignKey('Dqcheckdetails',on_delete=models.CASCADE)
    samplerow = models.TextField()
    runbatchid = models.ForeignKey('DqcheckRunBatch',on_delete=models.CASCADE)

class DqcheckRunFact(models.Model):
    dqcheckdetailid = models.ForeignKey('Dqcheckdetails',on_delete=models.CASCADE)
    measuredcount = models.BigIntegerField()
    totalcount = models.BigIntegerField()
    minvalue = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    maxvalue = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    avgvalue = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    runbatchid = models.ForeignKey('DqcheckRunBatch',on_delete=models.CASCADE)

    


    
