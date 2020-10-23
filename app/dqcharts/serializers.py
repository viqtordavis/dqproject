from rest_framework import serializers
from dqapp.models import Sourcedb,Connections,Connectiondetails,Dqrules,Dqcheck,Dqcheckdetails,DqcheckRunBatch,DqcheckRunFact



class DqcheckRunFactSerializer(serializers.Serializer):
    measuredcount = serializers.IntegerField()
    totalcount = serializers.IntegerField()
    minvalue = serializers.DecimalField(max_digits=11, decimal_places=2,required=False,default=0.00)
    maxvalue = serializers.DecimalField(max_digits=11, decimal_places=2,required=False,default=0.00)
    avgvalue = serializers.DecimalField(max_digits=11, decimal_places=2,required=False,default=0.00)
    tablename = serializers.CharField(max_length =100)
    columnname = serializers.CharField(max_length =100)
    dqrulename = serializers.CharField(max_length =100)
    

   