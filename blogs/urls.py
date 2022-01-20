from .views import SubscriptionCreateView
from django.conf.urls import re_path


app_name = 'blogs'
urlpatterns = [
    re_path(r'blogs/(?P<blog>[0-9]+)/subscribe', SubscriptionCreateView.as_view())
]
