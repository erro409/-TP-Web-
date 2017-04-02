from django.conf.urls import url

from task2.views import AboutView

urlpatterns = [
    url(r'^about$', AboutView.as_view(), name='about'),
]

