from django.shortcuts import render


def hello(request):
    return render(request, 'show/hello.html')


