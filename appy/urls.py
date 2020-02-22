from django.urls import path, include
from rest_framework import routers
from .views import AssignmentView, PendingTaskView, HostelView, AssignmentIDView
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()
# router.register('api/post', PostViewSet, 'post')
# router.register('api/calc', CalcView, 'calc')

# urlpatterns = router.urls

urlpatterns = format_suffix_patterns([
    path('api/assignment/', AssignmentView, name='assignment-view'),
    path('api/pending_task/', PendingTaskView, name='pending-task'),
    path('api/hostels/', HostelView, name='hotel-view'),
    path('api/assignment_id/', AssignmentIDView, name='assignment-id-view'),
])