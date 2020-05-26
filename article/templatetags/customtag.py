from django import template

register = template.Library()

@register.filter
def getContent(dict, sort):
    res = ""
    for item in dict:
        print(item.sort)
        if item.sort == sort:

            res =  item.content
            break

    return res

@register.filter
def getRange(res,num):
    return range(num)

@register.filter()
def to_int(value):
    return int(value)
