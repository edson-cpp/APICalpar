from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import UserViewSet, fetch_users_view

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch-users/', fetch_users_view, name='fetch-users')
]
