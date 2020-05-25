from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import ArticleType, Column, Content


def index(request):
    types = ArticleType.objects.all()
    return render(request, 'front/index.html', {'articleTypes': types})

def temp(request):
    return render(request, 'front/template1.html',  )


def test(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    else:
        print(request.POST.get('ab'))


def gs(request):
    id = request.GET.get('id', None)
    # articleType = ArticleType.objects.filter(id=id)[0]
    # print(articleType.column_set.all())

    articleTypes = ArticleType.objects.all()

    articleType = ArticleType.objects.filter(id=id)[0]

    # type = ArticleType.objects.filter(id=id)[0]

    # column = Column.objects.filter(id=22)[0]
    # res = Column.objects.select_related()
    # print(column.content_set.all())
    # for column in columns:
    #     contents = Content.objects.filter(column_id=column.id)
    #
    #     contents.append(Column.objects.filter(id=column.))
    return render(request, 'front/template2.html', {'articleTypes': articleTypes, 'articleType':articleType})