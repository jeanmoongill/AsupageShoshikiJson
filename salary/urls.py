from django.conf.urls import url

from salary.views import salaryTop, salaryInputView

urlpatterns = [

    #--------salary details------------------------------
    url(r'^salarytop/$', salaryTop.as_view(), name='SalaryTop'),


    #salary Input
    url(r'^salaryInput/$', salaryInputView.as_view(), name='salaryInput'),


]