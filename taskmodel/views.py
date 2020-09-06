from django.shortcuts import render,HttpResponse,redirect
from .models import table
# Create your views here.
def home(request):
    dict=table.objects.all()
    return render(request,"taskmodel/home.html",{'dict':dict})

def create(request):
    if request.method=='GET':
        dict=table.objects.all()
        return render(request,"taskmodel/home.html",{'dict':dict})
    else:
        input_text=request.POST['text']
        input_date=request.POST['date']
        d=table(text=input_text,date=input_date)
        d.save()
        return redirect(home)

def viewdata(request,data_pk):
    obj=table.objects.get(pk=data_pk)
    return render(request,"taskmodel/view.html",{'obj':obj})

def updatedata(request,data_pk):
    print("gfsdhsdfhf")
    obj=table.objects.get(pk=data_pk)
    if request.method=='GET':
        return render(request,"taskmodel/view.html",{'obj':obj})    
    obj.text=request.POST['text']
    obj.date=request.POST['date']
    obj.save()
    return redirect(home);

def deletedata(request,data_pk):
    obj=table.objects.get(pk=data_pk)
    obj.delete()
    return redirect('home')