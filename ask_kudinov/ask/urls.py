from django.conf.urls import url

from . import views
urlpatterns =[
   url(r'^$', views.index ,name = 'index'),
   url(r'^hot/', views.hot, name='hot'),
   url(r'^tag/(?P<tag>\S+)/?$', views.by_tag, name='by_tag'),
   url(r'^question/(?P<question_id>\d+)/$', views.question, name='question'),
   url(r'^login/', views.login , name = 'login'),
   url(r'^settings/', views.settings , name = 'settings'),
   url(r'^signup/', views.signup, name='signup'),
   url(r'^ask/', views.ask, name ='ask'),
]
