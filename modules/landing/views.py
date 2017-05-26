from django.shortcuts import render,redirect
from django.http import Http404
# Create your views here.
def index(request):
    return render(request,'landing/index.html')

def index_get_template(request,page):
    print(page)
    page = page + '.html'
    return render(request,'landing/'+page)