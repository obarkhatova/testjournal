from .views import AuthViewSet
from core.routers import get_url_routes

app_name = 'auth_'

urlpatterns = get_url_routes([('auth', AuthViewSet, 'auth')])

