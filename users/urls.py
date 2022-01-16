from .views import UserManagementViewSet
from core.routers import get_url_routes

app_name = 'users'

urlpatterns = get_url_routes([(r'users', UserManagementViewSet)])

