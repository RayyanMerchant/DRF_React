from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CalcView
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
# router = routers.DefaultRouter()
# router.register('api/post', PostViewSet, 'post')
# router.register('api/calc', CalcView, 'calc')

# urlpatterns = router.urls

urlpatterns = format_suffix_patterns([
    path('api/calc/', csrf_exempt(CalcView), name='calc-view')
])