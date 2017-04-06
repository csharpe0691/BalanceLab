from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginpage(request):
    return render(request, 'bLab/loginpage.html', {})

def selector(request):
    return render(request, 'bLab/selector.html', {})

def single_patient_search(request):
    return render(request, 'bLab/single_patient_search.html', {})

def single_patient_BR(request):
    return render(request, 'bLab/single_patient_BR.html', {})

def group_compar(request):
    return render(request, 'bLab/group_compar.html', {})

def group_report(request):
    return render(request, 'bLab/group_report.html', {})

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")