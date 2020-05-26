from django import forms
from django.forms import widgets
from django.utils.html import strip_tags
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from article.models import ArticleType, Column
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=8,
        label=' 文章标题'
    )
    content = SummernoteTextFormField(
        required=True,
        max_length=10240,
        label="文章内容"
    )
    type = forms.IntegerField(
        label="文章类别",
        widget=forms.Select(
            choices=ArticleType.objects.all().values_list('id', 'title')
        )
    )

class TypeForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        min_length=2,
        label=' 分类标题',
        widget = widgets.TextInput(attrs={'class': 'input-text'}),
        error_messages={
            'max_length': '输入的数据长度最大为20位',
            'min_length': '输入的数据长度最小为2位',
            'required': '数据不能为空'
        }
    )
    sort = forms.IntegerField(
        max_value=99,
        min_value=0,
        label='排序',
        widget=widgets.NumberInput(attrs={'class': 'input-text'}),
        error_messages={
            'max_value': '输入的数据最大为99',
            'min_value': '输入的数据不能小于0',
            'required': '数据不能为空',
            'invalid': '类型有误，只能输入数字',
        }
    )

max_length = 2048
content_error_messages = {
    'max_length': '输入的数据长度最大为'+str(max_length)+'位'
}
# class ContentForm(forms.Form):
#     content1 = forms.C

# class ColumnForm(forms.Form):
#     title = forms.CharField(
#         max_length=64,
#         widget=forms.TextInput(attrs={'class': 'input-text'}),
#         error_messages={
#             'max_length': "最大长度不能超过64位",
#             'required': "名称不能为空"
#         },
#     )

class ColumnForm(forms.Form):
    articleType = forms.IntegerField(
        required=True,
        widget=forms.Select(
            attrs={'class': 'select'},
            choices=ArticleType.objects.all().values_list('id', 'title')
        ),
        error_messages={
            'required': '必须选择一个选项'
        }
    )
    title = SummernoteTextFormField(
        required=True,
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'input-text'}),
        error_messages={
            'required': '栏目名不能为空'
        }
    )
    template = forms.IntegerField(
        required=True,
        widget=forms.Select(
            attrs={'class': 'select'},
            choices=[(1,'一行一列'), (2,'一行两列'), (3,'三行三列'),]
        ),

        error_messages={
            'required': '必须选择一个选项'
        }
    )
    isfluid= forms.IntegerField(
        required=True,
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[(1,'全部宽度'), (2,'两侧白边'),]
        ),
        error_messages={
            'required': '必须选择一个选项'
        },
        initial = [1,],
    )
    istitle= forms.IntegerField(
        required=True,
        widget=forms.RadioSelect(
            attrs={'class': 'radio'},
            choices=[(1,'显示标题栏'), (2,'隐藏标题栏'),]
        ),
        error_messages={
            'required': '必须选择一个选项'
        },
        initial=[1,]
    )
    sort = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class':'input-text'}),
        error_messages={
            'required': '排序值不能为空',
            'invalid': '必须输入一个整数'
        }
    )

class ContentForm(forms.Form):

    title = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput(attrs={'class':'input-text'}),
        error_messages={
            'required': '内容名不能为空'
        }
    )
    sort = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=9,
        widget=forms.NumberInput(attrs={'class':'input-text'}),
        error_messages={
            'required': '排序值不能为空',
            'invalid': '必须输入一个整数',
            'min_value': '最小数值为1',
            'max_value': '最大数值为9'
        }
    )

    content=SummernoteTextFormField(
        required=True,
        max_length=10240,
        error_messages={
            'required': '内容名不能为空'
        },
        widget=forms.TextInput(attrs={'class':'input-text'}),
    )
    column=forms.IntegerField(
        required=True,
        widget=forms.Select(
            attrs={'class': 'select'},
        ),
        error_messages={
            'required': '必须选择一个选项'
        }
    )
    # def __init__(self,*args, **kwargs):
    #     self.articleTypeId = kwargs.pop('articleTypeId', None)
    #     super(ContentForm, self).__init__(*args, **kwargs)
    #     qs = Column.objects.filter(articleType_id=self.articleTypeId).values_list('id',strip_tags( 'title'))
    #     qs2 = []
    #     for item in qs:
    #         qs2.append((item[0], strip_tags(item[1])))
    #     # print(qs2)
    #     self.fields['column'].widget.choices = qs2


    # content = forms.CharField(
    #     widget=SummernoteWidget(
    #         attrs={"style": "width:100%"}
    #     )
    # )
class BgImgForm(forms.Form):
    url=forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={'class': 'btn btn-secondary radius'}
        ),
        error_messages={
            'required': '必须选择好待上传的文件'
        }
    ),
    column = forms.IntegerField(
        required=True
    )

