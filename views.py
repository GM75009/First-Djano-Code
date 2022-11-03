#from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import *



# Create your views here.



# def func(request):
#     if request.method == 'POST':
#         name=request.POST.get("nm")
#         address=request.POST.get("add")
#         city=request.POST.get("city")
#         pincode=request.POST.get("pin")
#     print(name,address)
#     return HttpResponse("printed on console please check:")

def guru(request):

    if request.method == 'POST':

        a = request.POST.get("name")

        b = request.POST.get("address")

        c = request.POST.get("empID")


        d = table1(name=a,address=b,empID=c)

        d.save()
        print(a,b,c)


    else:

        return render(request,"page1.html",context={})

    return HttpResponse("printed on Console, please Check!!")


'''

def func2(request):
   
    
    return render(request,"page1.html",context={})

'''