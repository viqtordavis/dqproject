from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.dqcharts,name="dqmetrix"),
    path('<str:tablename>',views.quickprofile,name="quickprofile"),
    path('api/chartsdata/',views.apichartsdata,name="dqmetrix"),
]