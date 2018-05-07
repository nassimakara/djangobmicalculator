from django.conf.urls import url

from .import views

app_name = 'metric'


urlpatterns = [
        url(r'^minput/$', views.minput, name="minput"),
        url(r'^moutput/$', views.moutput, name="moutput"),
        url(r'^bmimetric/$', views.bmimetric, name="bmimetric"),
]
