from django.conf.urls import url
from docs import views

urlpatterns = [
    url(r'^$', views.DocsView.as_view(), name='docs'),
]