from django.shortcuts import render


def hello(request):
    return render(request, 'show/hello.html')

def index(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/index.html', context)

def login(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/login.html', context)

def register(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/register.html', context)

def hospitals(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/hospitals.html', context)

def contact(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/contact.html', context)

def list(request):
    context = {}
    context['key'] = "value"
    return render(request, 'show/list.html', context)