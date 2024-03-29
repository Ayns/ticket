from django.conf.urls import url
from django.urls import path

from log import views
# SET THE NAMESPACE!
app_name = 'log'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^tickets/$',views.tickets,name='tickets'),
    url(r'^newticket/$',views.newticket,name='newticket'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^home/$', views.home, name = 'home')
]
