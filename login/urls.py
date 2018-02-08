from . import views
from django.urls import path


from django.conf.urls import url


#urlpatterns = [
    #path('', views.index, name='index'),
#    path('ind/', views.ind, name='ind'),
    #path('main/', views.princ, name='princ'),
#    path('registro/', views.regist, name='regist'),
#path('main/', views.main, name='main'),
#path('', views, name='login'),

#]




app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^triviaa/$', views.triviaa, name='triviaa'),
    url(r'^returnn/$', views.returnn, name='returnn'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^details/(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.details.as_view(), name='details'),
    url(r'^processing/(?P<option>[-\w]+)-(?P<id>\d+)-(?P<ttlscore>\d+)/$', views.processing, name='processing'),
#Prueba mostrar datos
    url(r'^list/$', views.PersonaList.as_view(), name='plist'),

]
