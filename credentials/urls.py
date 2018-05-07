from django.conf.urls import url

from .import views

app_name = 'credentials'

urlpatterns = [

        url(r'^login/$', views.login_user, name="login"),
        url(r'^signup/$', views.signup, name="signup"),
        url(r'^logout/$', views.logout_user, name="logout"),
        url(r'^main/$', views.main, name="main"),

]
