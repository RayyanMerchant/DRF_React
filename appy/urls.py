from django.urls import path, include
from rest_framework import routers
from .views import AssignmentView, PendingTaskView, HostelView, AssignmentIDView, AssignmentAnsView, TeacherLeftView, TeacherCorrectView
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
    path('api/assignment_ans/', AssignmentAnsView, name='assignment-ans-view'),
    path('api/teacher_left/', TeacherLeftView, name='teacher-left-view'),
    path('api/teacher_correct/', TeacherCorrectView, name='teacher-correct-view')
])