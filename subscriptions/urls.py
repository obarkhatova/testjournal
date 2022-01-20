from .views import FeedView
from django.conf.urls import re_path


app_name = 'subscriptions'
urlpatterns = [
    re_path(r'feed', FeedView.as_view())
]
