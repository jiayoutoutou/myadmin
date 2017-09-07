from django.shortcuts import render,HttpResponse
from django.urls import reverse

class MyModelAdmin:
    list_display = "__all__"
    def __init__(self, model, admin_site):
        self.model = model
        self.admin_site = admin_site

    @property
    def urls(self):
        return self.get_urls()
    def get_urls(self):
        from django.conf.urls import url
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view, name='%s_%s_changelist' % info),
            # url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            # url(r'^(.+)/delete/$', self.delete_view, name='%s_%s_delete' % info),
            url(r'^(.+)/change/$',self.change_view, name='%s_%s_change' % info),
        ]
        return urlpatterns
    def change_view(self,request,pk):
        return HttpResponse('垃圾')
    def changelist_view(self,request):
        # print(request.path)
        # print(request.resolver_match,type(request.resolver_match),type(request.resolver_match.url_name))
        result_list=self.model.objects.all()
        return render(request,'changelist.html',{'result_list':result_list,'list_display':self.list_display,'model_admin':self})
class MyAdminSite:

    def __init__(self,name='myadmin'):
        self._registry = {}  # model_class class -> admin_class instance
        self.name = name

    def register(self, model_or_iterable, admin_class=None, **options):
        if not admin_class:
            admin_class = MyModelAdmin
        self._registry[model_or_iterable]=admin_class(model_or_iterable,self)

    def get_urls(self):
        from django.conf.urls import url, include
        # Admin-site-wide views.
        urlpatterns = [
            # url(r'^$', self.index, name='index'),
            url(r'^login/$', self.login, name='login'),
        ]
        for model, model_admin in self._registry.items():
            urlpatterns += [
                # url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), self.login),
                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'admin', self.name

    def login(self,request):
        return HttpResponse("垃圾")

site=MyAdminSite()
