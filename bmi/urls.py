from django.conf.urls import url, include
from django.contrib import admin
from .import views

app_name = 'bmi'

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^credentials/', include('credentials.urls')),
        url(r'^metric/', include('metric.urls')),
        url(r'^imperial/', include('imperial.urls')),
        url(r'^$', views.welcome, name="welcome"),
        url(r'^aboutus/', views.aboutus, name="aboutus"),
        url(r'^bmi/', views.bmi, name="bmi"),


]
