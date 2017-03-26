
from django.conf.urls import include, url
from .views import AccountLogin
from .views import to_top, logout_view

urlpatterns = [

    #--------login-----------------------------
    url(r'^login/$', AccountLogin.as_view(
        template_name = 'index.html'
    ), name='login_page'),

    #--------top------------------------------
    url(r'^top/$', to_top, name='top_page'),

    #--------logout---------------------------
    url(r'^logout/$', logout_view, name='logout')


]