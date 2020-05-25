import hashlib
import os
import time

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from article.models import ArticleType
from lib.lib import my_md5
from login.models import Users, UserInfo


def login(request):
    if request.session.get("username"):
        return redirect("/login/index/")
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        # if username == 'admin' and password == "123":

        # md5 = hashlib.md5()
        # md5.update(password.encode())
        # pw = md5.hexdigest()

        pw = my_md5(password)
        rs = Users.objects.filter(username=username, password=pw)
        print(rs)
        if rs:
            request.session['username'] = username
            request.session['userid'] = rs[0].id
            return HttpResponse("1")
        else:
            return HttpResponse("2")


def index(request):
    if request.session.get("username"):
        types = ArticleType.objects.all()
        return render(request, 'index.html', {"types": types})
    else:
        return redirect("/login/denglu/")


def welcome(request):
    return render(request, 'welcome.html')


def exit(request):
    del request.session['username']
    del request.session['userid']
    return redirect('/login/denglu/')


def init(request):
    users = Users()
    users.username = "admin222"

    # md5 = hashlib.md5()
    # md5.update('初始化完成！'.encode())
    # pw = md5.hexdigest()
    pw = my_md5("222")
    users.password = pw
    users.save()
    return HttpResponse("初始化完成！")

class UserInfoForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-text'}),
        error_messages={
            'max_length': "最大长度不能超过100",
            'required': "不能为空"
        }
    )
    birthday = forms.DateField(
        input_formats= ['%Y-%m-%d'],
        widget=forms.DateInput(attrs={"onclick": "WdatePicker()", "class": "input-text"}),
        error_messages={
            'invalid': "格式不正确"
        }
    )
    email = forms.EmailField(
        required=False,
        error_messages={
            'invalid': "必须输入邮箱格式"
        },
        # widget=forms.EmailInput()
    )
    thumb = forms.FileField(
        required=False,
        max_length=100,
        widget=forms.FileInput(attrs={"accept": ".jpg,.png"}),

    )
    gender = forms.IntegerField(
        required=True,
        widget=forms.Select(attrs={'class': "select"}, choices=((1, '男'), (2, '女'))),
        error_messages={
            'required': '不能为空'
        }
    )
    hobby = forms.MultipleChoiceField(
        required=True,
        choices=((1, '上网'), (2, '旅游'), (3,'读书')),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
        error_messages={
            'required': '不能为空'
        }
    )
    pos = forms.IntegerField(
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'radio'}, choices=((1, '国内'), (2, '国外'))),
        error_messages={
            'required': '不能为空'
        }
    )

def userinfo(request):
    if request.method == 'GET':
        userInfoForm = UserInfoForm()
        userInfoForm.initial = {'gender': 2}
        return render(request, 'user-info.html', {'userInfoForm': userInfoForm})
    else:
        # userInfoForm = UserInfoForm()
        userInfoForm = UserInfoForm(request.POST, request.FILES)
        if userInfoForm.is_valid():
            print(userInfoForm.cleaned_data)
            file = request.FILES['thumb']
            filename = str(int(time.time())) + os.path.splitext(file.name)[1]
            tofile = os.path.join('media/upload/', filename)
            f = open(tofile, 'wb')
            for chunk in file:
                f.write(chunk)
            f.close()
            data = userInfoForm.cleaned_data
            data['thumb'] = "/"+tofile
            res = UserInfo.objects.create(**data)
            id = request.session.get('userid')
            user = Users.objects.filter(id=id)[0]
            user.userinfo = res
            user.save()
            return HttpResponse("ok")
        else:
        # print(request.POST.get('birthday'))
            print(userInfoForm.errors)
            return HttpResponse(userInfoForm.errors)


def userinfoup(request):
    if request.method == 'GET':
        id = request.session.get('userid', None)
        user = Users.objects.filter(id=id)[0]
        userInfoForm = UserInfoForm(initial={
            'username': user.userinfo.username,
            'birthday': user.userinfo.birthday,
            'email': user.userinfo.email,
            'thumb': user.userinfo.thumb,
            'gender': user.userinfo.gender,
            'hobby': list(user.userinfo.hobby),
            'pos': user.userinfo.pos
        })
        # userInfoForm.fields['thumb'].required = False
        return render(request, 'user-info.html', {'userInfoForm':userInfoForm, 'id': user.userinfo.id})
    else:

        userInfoForm = UserInfoForm(request.POST, request.FILES)
        # userInfoForm.fields['thumb'].required = False
        if userInfoForm.is_valid():
            data = userInfoForm.cleaned_data
            thumb = data.get('thumb', None)
            if not thumb:
                del data['thumb']
            else:

                file = request.FILES['thumb']
                filename = str(int(time.time())) + os.path.splitext(file.name)[1]
                tofile = os.path.join('media/upload/', filename)
                f = open(tofile, 'wb')
                for chunk in file:
                    f.write(chunk)
                f.close()
                data = userInfoForm.cleaned_data
                data['thumb'] = "/" + tofile

            userinfo = UserInfo.objects.filter(id=request.POST.get('id'))
            userinfo.update(**data)
            print(data)
        else:
            print(userInfoForm.errors)
        return HttpResponse("up")