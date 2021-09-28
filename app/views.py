from django.shortcuts import render

# Create your views here.
from app.forms import *

def register(request):
    userform=UserForm()
    profileform=ProfileForm()


    d={'userform':userform,'profileform':profileform}
    return render(request,'register.html',d)