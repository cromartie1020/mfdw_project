from django.shortcuts import render
from django.contrib.auth import login, authenticate   
from django.contrib.auth.forms import UserCreationForm 
def signin(request):
    if request.method=='POSt':
        form = UserCreationForm(request.POST)

    else:
        form=UserCreationForm()
    context={
        'form':form
    }    
    return render(request,'accounts/signup.html',context)        

