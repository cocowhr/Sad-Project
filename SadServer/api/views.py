from django.shortcuts import render

# Create your views here.
def test(request):
    if 'name' in request.GET:
        name=request.GET['name']
        print (name)