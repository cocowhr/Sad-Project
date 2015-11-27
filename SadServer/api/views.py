from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import *

# Create your views here.
@csrf_exempt
def register(request):
    name = request.POST['name']
    idcard = request.POST['idcard']
    contact = request.POST['contact']
    password = request.POST['password']
    # 密码检验如何弄？

    # 判断用户名是否被注册
    try:
        context = {}
        context['key'] = "value"
        User.objects.get(name=name)
        return render(request, 'show/hello.html', context)
        # 判断用户名是否被注册
    except ObjectDoesNotExist:
        User.objects.create(name=name, passwd=password, contact=contact)
        return render(request, 'show/index.html', context)


@csrf_exempt
def login(request):
    name = request.POST['name']
    password = request.POST['password']
    # 判断用户名是否被注册
    try:
        context = {}
        context['key'] = "value"
        user = User.objects.get(name=name)
        if (user.passwd != password):
            return render(request, 'show/login.html', context)
        return render(request, 'show/hello.html', context)
        # 判断用户名是否被注册
    except ObjectDoesNotExist:
        return render(request, 'show/register.html', context)


@csrf_exempt
def searchhospname(request):
    hospname = request.GET["hospname"]
    hosplist = Hospital.objects.filter(name__contains=hospname)
    if hosplist.__len__() > 0:
        context = {}
        context['hospitalList'] = []
        for hosp in hosplist:
            hosp1 = {}
            hosp1['id'] = hosp.id
            hosp1['name'] = hosp.name
            hosp1['loc'] = hosp.address
            hosp1['intro'] = hosp.contact
            context['hospitalList'].append(hosp1)
        return render(request, 'show/hospitals.html', context)
        # 判断用户名是否被注册
    else:
        context = {}
        return render(request, 'show/hello.html', context)


@csrf_exempt
def searchdepartment(request, hospitalid):
    try:
        deplist = Department.objects.filter(hospital=hospitalid)
        context = {}
        context['departments'] = []
        for dep in deplist:
            dep1 = {}
            dep1['id'] =dep.id
            dep1['name'] =dep.name
            dep1['doctors']=[]
            doclist=Doctor.objects.filter(department=dep.id)
            for doc in doclist:
                doc1={}
                doc1['name'] =doc.name
                doc1['price'] =doc.contact
                dep1['doctors'].append(doc1)
            context['departments'].append(dep1)
        return render(request, 'show/orders.html', context)
    except ObjectDoesNotExist:
        return render(request, 'show/hello.html', context)