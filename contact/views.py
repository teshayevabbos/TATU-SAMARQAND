from django.shortcuts import render,HttpResponse,redirect
from .models import *

def ContactView(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    ContactModel.objects.create(name=name,email=email,subject=subject,message=message)
    return redirect('home')
  return render(request,'contact/contact.html')


def TeacherView(request):
  context = TeacherModell.objects.all()
  return render(request,'contact/services.html',{'context':context})


def TeachersInfoView(request,name):
  obj = InfoModell.objects.get(name=name)
  return render(request,'contact/info.html',{'obj':obj})