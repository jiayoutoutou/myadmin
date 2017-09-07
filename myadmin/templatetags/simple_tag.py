from django.template import Library
from types import FunctionType

# def inner(result_list,list_display):
#     for item in result_list:
#         yield [getattr(item, name) for name in list_display]
register=Library()
@register.inclusion_tag('table.html')
def func(result_list,list_display,model_admin):
    def tbody():
        for item in result_list:
            yield [name(model_admin,item.pk) if isinstance(name,FunctionType) else getattr(item, name) for name in list_display]
    def thead():
        for title in list_display:
            yield title.__name__.title() if isinstance(title,FunctionType) else title
    return {"tbody":tbody(),"thead":thead()}