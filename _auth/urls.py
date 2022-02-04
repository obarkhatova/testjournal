from .views import AuthViewSet
from core.routers import get_url_routes

app_name = '_auth'

urlpatterns = get_url_routes([('auth', AuthViewSet, 'auth')])

