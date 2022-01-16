from .views import PostViewSet
from core.routers import get_url_routes

app_name = 'posts'

urlpatterns = get_url_routes([
    ('posts', PostViewSet),
])
