import json

from django import forms
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import Users


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=8,
        min_length=2,
        required=True,
        error_messages={
            'max_length': '输入的数据长度最大为8位',
            'min_length': '输入的数据长度最小为2位',
            'required': '数据不能为空'
        }
    )
    password = forms.CharField(
        max_length=8,
        min_length=4,
        required=True
    )

def form1(request):
    if request.method == 'GET':
        userform = UserForm()
        return render(request, 'form1.html', {'userform': userform})
    else:
        userform = UserForm(request.POST)
        if userform.is_valid():
            data = userform.cleaned_data
            Users.objects.create(**data)
            return HttpResponse("ok")
        else:
            # print(userform.errors['username'][0])
            # print(userform.errors['password'][0])
            return render(request, 'form1.html', {'userform': userform})


def ajaxform(request):
    res = {'status': True, 'msg': None}
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            data = userform.cleaned_data
            print(data)
            return HttpResponse("ok")
        else:
            res['status'] = False
            res['msg'] = userform.errors

            return HttpResponse(json.dumps(res))
    else:
        return HttpResponse("test")


def updateform(request):
    if request.method == "GET":
        user = Users.objects.filter(id=2)[0]
        print(type(user))
        userform = UserForm(initial=model_to_dict(user))
        return render(request, 'form1.html', {'userform': userform})
    else:
        userform = UserForm(request.POST)
        if userform.is_valid():
            data = userform.cleaned_data
            # thumb = data.get('thumb', None)
            # if not thumb:
            #     del data['thumb'] =
            Users.objects.filter(id=2).update(**data)
            return HttpResponse("ok")
        else:
            return render(request, 'form1.html', {'userform': userform})
