from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import *



# Create your views here.



# def func(request):
#     if request.method=='POST':
#         Name=request.POST.get('nm')
#         Address=request.POST.get('add')
#         City=request.POST.get('city')
#         PINCODE=request.POST.get('pin')
#         a = Sneha(Name,Address,City,PINCODE)
#         a.save()
#         print(Name)
#         print(Address)
#         print(City)
#         print(PINCODE)

#     else:

#         return render(request,"page1.html",context={})

#     return HttpResponse("printed on Console, please Check!!")

#         #return redirect("page2")

# def func2(request):

#     a=Sneha()

#     b=Sneha.objects.all()

#     # c=Kiran.objects.filter(empID=12335)

#     print(b)   

#     return render(request,"page1.html",context={})
def func3(request):
    if request.method == 'POST':
        a = request.POST.get("name")
        b = request.POST.get("address")
        c= request.POST.get("empID")
        d = Sneha(name=a,address=b,empID=c)
        d.save()
        print(a,b,c)
        
    else:
        return render(request,"page2.html",context={})

    return HttpResponse("printed on Console, please Check!!")