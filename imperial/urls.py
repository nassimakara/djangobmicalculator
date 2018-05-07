from django.conf.urls import url

from .import views

app_name = 'imperial'


urlpatterns = [
        url(r'^impinput/$', views.impinput, name="impinput"),
        url(r'^impoutput/$', views.impoutput, name="impoutput"),
        url(r'^bmiimperial/$', views.bmiimperial, name="bmiimperial"),
]
