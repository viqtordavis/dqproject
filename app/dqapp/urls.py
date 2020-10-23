from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('fileupload/',views.fileupload.as_view(),name="fileupload"),
    path('runfileprofile/',views.runfileprofile,name="runfileprofile"),
    path('newconnection/',views.newconnection.as_view(),name="newconnection"),
    path('newconnection/addconnection',views.addconnection.as_view(),name="addconnection"),
    path('newdqcheck/',views.newdqcheck.as_view(),name="newdqcheck"),
    path('newdqcheck/adddqcheck',views.adddqcheck.as_view(),name="adddqcheck"),
    path('ajax/load-tables/',views.loadtables,name="loadtables"),
    path('ajax/load-form/',views.addconnection.as_view(),name="loadform"),
    path('ajax/loadcolumnNrules/',views.loadcolumnNrules,name="loadcolumnNrules"),
    path('rundqcheck/',views.rundqcheck.as_view(),name="rundqcheck"),
    path('rundqcheck/rundq/',views.rundqcheck.as_view(),name="rundq"),
    path('ajax/loadbatchrun/',views.loadbatchrun,name="loadbatchrun"),

]

