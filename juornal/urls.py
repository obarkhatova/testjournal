from django.conf.urls import include, re_path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^api/', include('auth.urls')),
    re_path(r'^docs/', include('docs.urls')),
    re_path(r'^api/', include('posts.urls')),
    re_path(r'^api/', include('users.urls')),
    re_path(r'^api/', include('blogs.urls')),
    re_path(r'^api/', include('subscriptions.urls')),
]


