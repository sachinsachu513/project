from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import employees
from .form import employeeform

# Create your views here.
def greetings(request):
    msg="<h1> Welcome to my my django project </h1>"
    return HttpResponse (msg)
def table(request):
    emp=employees .objects.all()
    return render(request,'student/table.html',context={"emp":emp})

def createemployees(request):
    form=employeeform()
    if request.method =="POST":
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("""<h1> new employ data sucessfully added </h1>

                      <h1> <a href="/tab"> click here </a>view employ details</h2>



                      """

                                )
    return render(request,'student//addemployees.html',context={'form':form})


def deleteemploy(request,id):
    emp=employees.objects.get(id=id)
    emp.delete()
    return redirect('/tab')


def updateemploy(request,id):
    emp=employees.objects.get(id=id)
    if request.method=='POST':
        form=employeeform(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponse("""<h1> employ data updated suceesfully </h1>

                     <h1> <a href="/tab"> click here </a>view employ details</h2>
                   """)
    return render(request,"student//update.html", context={"emp": emp})




