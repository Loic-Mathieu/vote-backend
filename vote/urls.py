from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


app_name = 'vote'

# Pages accessibles
router = routers.DefaultRouter()
router.register(r'candidats', views.TestViewSet)
router.register(r'votes', views.VoteViewSet)
router.register(r'utilisateurs', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
