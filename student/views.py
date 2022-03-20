from django.shortcuts import render
# from django.http import HttpResponse
# from student.models import contact 

# from .models import contact
# Create your views here.
def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def education(request):
    return render (request,'education.html')

