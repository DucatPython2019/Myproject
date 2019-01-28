from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp
# Create your views here.
def index(request):
	return render(request,'index.html')
def register_input(request):
	return render(request,'register_input.html')
def register_db(request):
	n=request.POST.get('name','')
	s=request.POST.get('sal','')
	email=request.POST.get('email','')
	e=emp(name=n,sal=s,email=email)
	e.save()
	return render(request,'register_input.html',{'msg':'Record inserted..'})
def view(request):
	emps=emp.objects.all()
	return render(request,'showdata.html',{'data':emps})
def edit(request):
	id=request.GET.get('id','')
	e=emp.objects.get(id=id)	
	return render(request,'edit.html',{'emp':e})
def update_db(request):
	n=request.POST.get('name','')
	s=request.POST.get('sal','')
	email=request.POST.get('email','')
	id=request.POST.get('id','')
	e=emp.objects.get(id=id)
	e.name=n
	e.sal=s
	e.email=email
	e.save()
	return render(request,'edit.html',{'msg':'Record updated...'})
def delete(request):
	id=request.GET.get('id','')
	e=emp.objects.get(id=id)
	e.delete()
	return redirect('/view')