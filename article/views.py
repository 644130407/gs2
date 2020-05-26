import json
import os
import time

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.form import ArticleForm, TypeForm, ContentForm, ColumnForm, BgImgForm
from article.models import ArticleType, Article, Column, Content, BackImg
from login.models import Users


def articlelist(request):
    articles = Article.objects.all()
    return render(request, 'article-list.html', {'articles': articles})


def articleadd(request):
    if request.method == 'GET':
        types = ArticleType.objects.all()
        return render(request, 'article-add.html', {'types': types})
    else:
        # title = request.POST.get('articletitle')
        # type = request.POST.get('articletype')
        # content = request.POST.get('content')
        # author = request.session.get('userid')
        #
        # print(title)
        # print(type)
        # print(content)
        # print(author)
        #
        # article = Article()
        # article.title = title
        # article.type = ArticleType.objects.filter(id=type)[0]
        # article.content = content
        # article.author = Users.objects.filter(id=author)[0]
        # article.save()

        af = ArticleForm(request.POST)
        if af.is_valid():
            data = af.cleaned_data
            Article.objects.create(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '恭喜你，文章已经成功添加！',
                              'url': '/article/articlelist/'
                          })
        else:
            print(af.errors)
            return HttpResponse("error")


def init(request):
    ArticleType.objects.all().delete()
    try:
        ArticleType(title='首页').save()
        ArticleType(title='集团介绍').save()
        ArticleType(title='国际学校 - 美达菲').save()
        ArticleType(title='普教 - 南开区美达菲中学').save()
        ArticleType(title='普教-名仁初级中学').save()
        ArticleType(title='职业教育').save()
        ArticleType(title='六十八所').save()
        ArticleType(title='联系我们').save()

    except:
        return HttpResponse('初始化失败，文章类型已完成过初始化！')
    return HttpResponse('ok')


def articleedit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        article = Article.objects.filter(id=id)[0]
        types = ArticleType.objects.all()
        return render(request, 'article-edit.html', {'article': article, 'types': types})
    else:
        id = request.POST.get('id')
        typeid = request.POST.get('articletype')
        title = request.POST.get('articletitle')
        content = request.POST.get('content')
        type = ArticleType.objects.filter(id=typeid)[0]

        article = Article.objects.filter(id=id)[0]
        article.title = title
        article.content = content
        article.type = type
        article.save()

        return render(request, 'sucess.html',
                      {
                          'info': '恭喜你，文章已经成功修改！',
                          'url': '/article/articlelist/'
                      })


def articledel(request):
    id = request.POST.get('id')
    article = Article.objects.filter(id=id)[0]
    try:
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
    # return None


def testadd(request):
    af = ArticleForm()
    return render(request, 'testadd.html', {'af': af})


def typelist(request):
    if request.method == 'GET':
        types = ArticleType.objects.order_by('sort').all()

        return render(request, 'type-list.html', {'types': types})


def typeadd(request):
    if request.method == 'GET':
        typeForm = TypeForm()
        btns = list(range(0, 9))
        return render(request, 'type-add.html', {'tf': typeForm, 'btns': btns})
    else:
        typeForm = TypeForm(request.POST)
        if typeForm.is_valid():
            data = typeForm.cleaned_data
            ArticleType.objects.create(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '恭喜你，分类已经成功添加！',
                              'url': '/article/typelist/'
                          })
        else:
            return render(request, 'type-add.html', {'tf': typeForm})


def columnlist(request):
    if request.method == 'GET':
        columns = Column.objects.all().order_by('-id')
        articleTypeId = request.GET.get('articleTypeId')
        return render(request, 'column-list.html', locals())
    return None


# 栏目添加
def columnadd(request):
    if request.method == 'GET':
        columnForm = ColumnForm()
        return render(request, 'column-add.html', {'columnForm': columnForm})
    else:
        columnForm = ColumnForm(request.POST)
        if columnForm.is_valid():
            data = columnForm.cleaned_data
            id = data.get('articleType', None)
            data['articleType'] = ArticleType.objects.filter(id=id)[0]
            print(data)
            try:
                res = Column.objects.create(**data)
                print('res:')
                print(res.id)
                return render(request, 'sucess.html',
                              {
                                  'info': '恭喜你，栏目已经成功添加！',
                                  'url': '/article/columnlist/',
                              })
            except Exception as e:
                print(e)
                return render(request, 'sucess.html',
                              {
                                  'info': '栏目添加失败！',
                                  'url': '/article/columnlist/'
                              })
        else:
            print(columnForm.errors)
            return render(request, 'column-add.html', locals())


def contentlist(request):
    if request.method == 'GET':
        articleTypeId = request.GET.get('articleTypeId')
        columnId = request.GET.get('columnId')
        # imgbg = BackImg.objects.filter(column_id__exact=columnId)[0].get('url',None)
        print("list:")
        print(columnId)
        print("list2")
        # print(imgbg)
        contents = Content.objects.all()
        # print(articleTypeId)
        # columnId = request.POST.get('column')
        # column = Content.objects.filter(column=columnId)
        # bg = BackImg.objects.filter(column=columnId)
        return render(request, 'content-list.html', locals())
    return None


def subcontentlist(request):
    if request.method == 'GET':
        articleTypeId = request.GET.get('articleTypeId')
        columnId = request.GET.get('columnId')
        imgfield = BackImg.objects.order_by('-id').filter(column_id=columnId)
        print(imgfield.exists())
        imgbg = imgfield[0].url if imgfield.exists() else None
        print(imgbg)

        print("list:")
        print(columnId)
        contents = Content.objects.filter(column=columnId)
        # print(articleTypeId)
        # columnId = request.POST.get('column')
        # column = Content.objects.filter(column=columnId)
        # bg = BackImg.objects.filter(column=columnId)
        return render(request, 'content-list.html', locals())
    return None


def contentadd(request):
    if request.method == 'GET':
        columnId = request.GET.get('columnId', None)
        print(columnId)
        contentForm = ContentForm()
        articleType = Column.objects.filter(id=columnId)[0].articleType.id
        columns = Column.objects.filter(articleType_id=articleType)
        return render(request, 'content-add.html', {'contentForm': contentForm, 'columns':columns, 'columnId': columnId})
    else:
        cf = ContentForm(request.POST)
        if cf.is_valid():
            data = cf.cleaned_data
            columnId = data.get('column')

            data['column'] = Column.objects.filter(id=data['column'])[0]
            articleTypeId = Column.objects.filter(id=columnId)[0].articleType.id
            try:
                Content.objects.create(**data)
                return render(request, 'sucess.html',
                              {
                                  'info': '恭喜你，内容已经成功添加！',
                                  'url': '/article/subcontentlist/?articleTypeId=' + str(
                                      articleTypeId) + '&columnId=' + str(columnId)
                              })
            except Exception as e:
                return render(request, 'sucess.html',
                              {
                                  'info': '内容添加失败！',
                                  'url': '/article/subcontentlist/?articleTypeId=' + str(
                                      articleTypeId) + '&columnId=' + str(columnId)
                              })
        else:

            columnId = cf.cleaned_data.get('column', None)
            articleType = Column.objects.filter(id=columnId)[0].articleType.id
            columns = Column.objects.filter(articleType_id=articleType)
            # contentForm.errors = cf.errors
            return render(request, 'content-add.html',
                          {'contentForm': cf, 'columns': columns, 'columnId': columnId})


def uploadbg(request):
    if request.method == "POST":
        bgImgForm = BgImgForm(request.POST, request.FILES)
        if bgImgForm.is_valid():
            data = bgImgForm.cleaned_data
            file = request.FILES.get('url', None)
            filename = str(int(time.time())) + os.path.splitext(file.name)[1]
            tofile = os.path.join('static/upload/', filename)
            f = open(tofile, 'wb')
            for chunk in file:
                f.write(chunk)
            f.close()
            data['url'] = os.path.join('upload/', filename)
            data['column'] = Column.objects.filter(id=data['column'])[0]
            BackImg.objects.create(**data)
            res = {'status': 'ok', 'url': data['url']}
            return HttpResponse(json.dumps(res))
        else:
            print(bgImgForm.errors)
        # data['column'] = Column.objects.filter(id=request.POST.get('column', None))[0]
        # BackImg.objects.create(**data)

    return None


def typeedit(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        data = ArticleType.objects.filter(id=id)[0]
        typeForm = TypeForm(initial=model_to_dict(data))
        return render(request, 'type-add.html', {'tf': typeForm, 'id': id})
    else:
        typeForm = TypeForm(request.POST)
        if typeForm.is_valid():
            data = typeForm.cleaned_data
            print(data)
            ArticleType.objects.filter(id=request.POST.get('id')).update(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '修改成功！',
                              'url': '/article/contentlist/'
                          })


def typedel(request):
    id = request.POST.get('id')
    articleType = ArticleType.objects.filter(id=id)[0]
    try:
        articleType.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


def columnedit(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        data = Column.objects.filter(id=id)[0]
        columnForm = ColumnForm(initial=model_to_dict(data))
        return render(request, 'column-add.html', {'columnForm': columnForm, 'id': id})
    else:
        columnForm = ColumnForm(request.POST)
        if columnForm.is_valid():
            data = columnForm.cleaned_data
            print(data)
            data['articleType'] = ArticleType.objects.filter(id=data['articleType'])[0]
            Column.objects.filter(id=request.POST.get('id')).update(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '修改成功！',
                              'url': '/article/columnlist/'
                          })


def columndel(request):
    id = request.POST.get('id')
    column = Column.objects.filter(id=id)[0]
    try:
        column.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


def contentedit(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        data = Content.objects.filter(id=id)[0]
        # data['column'] = Column.objects.filter(id=data['column'])[0]
        contentForm = ContentForm(initial=model_to_dict(data))
        column = Content.objects.filter(id=id)[0].column
        articleTypeId = column.articleType.id
        columns = Column.objects.filter(articleType_id=articleTypeId)
        return render(request, 'content-add.html',
                      {'contentForm': contentForm, 'columns': columns, 'columnId': column.id, 'id':id})
    else:
        contentForm = ContentForm(request.POST)
        if contentForm.is_valid():
            data = contentForm.cleaned_data
            id = request.POST.get('column', None)
            data['column'] = Column.objects.filter(id=id)[0]
            articleTypeId = data['column'].articleType.id
            print(request.POST.get('id'))
            Content.objects.filter(id=request.POST.get('id')).update(**data)
            return render(request, 'sucess.html',
                          {
                              'info': '修改成功！',
                              'url': '/article/subcontentlist/?columnId=' + str(id) + '&articleTypeId=' + str(
                                  articleTypeId)
                          })
        else:
            columnId = contentForm.cleaned_data.get('column', None)
            articleType = Column.objects.filter(id=columnId)[0].articleType.id
            columns = Column.objects.filter(articleType_id=articleType)
            # contentForm.errors = cf.errors
            return render(request, 'content-add.html',
                          {'contentForm': contentForm, 'columns': columns, 'columnId': columnId, "id":request.POST.get('id')})



def contentdel(request):
    id = request.POST.get('id')
    content = Content.objects.filter(id=id)[0]
    try:
        content.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
