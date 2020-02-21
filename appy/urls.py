from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CalcViewSet

router = routers.DefaultRouter()
router.register('api/post', PostViewSet, 'post')
router.register('api/calc', CalcViewSet, 'calc')

urlpatterns = router.urls
