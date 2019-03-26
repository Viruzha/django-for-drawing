from django.shortcuts import render
from mapping.models import Data1
from datetime import datetime
from django.db.models import Q

import json

def mapping(request):
    list1=list(range(7,24))
    return render(request,'index.html',context={'list': list1})

def draw(request,a):
    if a==23:
        data=Data1.objects.filter(Q(time__gt=datetime(2014,8,3,23,0,0))&Q(time__lt=datetime(2014,8,3,23,59,59)))
    else:
        data=Data1.objects.filter(Q(time__gt=datetime(2014,8,3,a,0,0))&Q(time__lt=datetime(2014,8,3,a+1,0,0)))
    mapdotx=[]
    mapdoty=[]
    mapc=[]
    for i in data:
        y=700-(i.lat-30.2911091)/0.7045307*800
        x=(i.lon-103.4971466)/1.1105957*1400-200
        mapdotx.append(x)
        mapdoty.append(y)
        mapc.append(i.ex)
    return render(request,'map.html',context={'mapdotx':json.dumps(mapdotx),'mapdoty':json.dumps(mapdoty),'mapc':json.dumps(mapc)})


# Create your views here.
