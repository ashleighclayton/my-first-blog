from django.conf.urls import url, patterns, include
from .import views
from .views import TimeSeriesView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^data', TimeSeriesView.as_view(), name='data'),
]
