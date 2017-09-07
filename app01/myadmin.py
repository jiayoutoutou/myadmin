print('myadmin')
from django.utils.safestring import mark_safe
from django.urls import reverse
from app01.models import UserInfo
from myadmin.service import mysite
class UserInfoModelAdmin(mysite.MyModelAdmin):
    def edit(self,pk):
        name="{0}:{1}_{2}_change".format(self.admin_site.name,self.model._meta.app_label, self.model._meta.model_name)
        url=reverse(name,args=(pk,))
        return mark_safe("<a href='{0}'>编辑</a>".format(url))
    list_display=['id','user','email',edit]
mysite.site.register(UserInfo,UserInfoModelAdmin)