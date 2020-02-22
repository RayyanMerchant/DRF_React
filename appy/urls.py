from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CalcView, AssignmentView
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()
# router.register('api/post', PostViewSet, 'post')
# router.register('api/calc', CalcView, 'calc')

# urlpatterns = router.urls

urlpatterns = format_suffix_patterns([
    path('api/calc/', CalcView, name='calc-view'),
    path('api/assignment/', AssignmentView, name='assignment-view'),
])