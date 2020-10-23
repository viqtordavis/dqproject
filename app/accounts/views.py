from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.views import LoginView



# Create your views here.

class loginview(LoginView):
    def get(self, request, *args, **kwargs):
        global redirect_to
        redirect_to=self.request.GET.get('next')
        print(redirect_to)
        return render(request,'login.html')
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(redirect_to)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if redirect_to is None:
                return redirect('/')
            else:
                return redirect(redirect_to)
        else:
            messages.info(request,"Invalid Credentials. Please Enter Correct Username and Password")
            return redirect('login')
# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
    
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,"Invalid Credentials")
#             return redirect('login')
#     else:
#         return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')