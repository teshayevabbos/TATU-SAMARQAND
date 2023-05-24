from django.shortcuts import render
from .models import *

def TeamView(request):
    team = TeamModel.objects.all()
    return render(request,'team/team.html',{'team':team})