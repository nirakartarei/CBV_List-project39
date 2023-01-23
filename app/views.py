from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import View,ListView

class Home(View):
    def get(self,request):
        return render(request,'app/home.html')

class School_list(ListView):
    model=School
    context_object_name='schools'
    #ordering=['name']