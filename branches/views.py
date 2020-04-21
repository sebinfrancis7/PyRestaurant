from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch
# Create your views here.

def branches(request):
    branches = Branch.objects.all()
    return render(request, 'branch.html', {'branches': branches})


