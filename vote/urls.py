from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'vote'

# Pages accessibles
router = routers.DefaultRouter()
router.register(r'candidats', views.TestViewSet)
router.register(r'votes', views.VoteViewSet)
router.register(r'utilisateurs', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
