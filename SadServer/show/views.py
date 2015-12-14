from django.shortcuts import render
from api.models import *


def hello(request):
    return render(request, 'show/hello.html')


def index(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/index.html', context)


def login(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/login.html', context)


def register(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/register.html', context)


def hospitals(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/hospitals.html', context)


def contact(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/contact.html', context)


def list(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/list.html', context)


def backstage(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/backstage.html', context)

def info(request):
    context = {}
    try:
        context['name'] = request.session['username']
    finally:
        return render(request, 'show/info.html', context)
