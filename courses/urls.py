from django.urls import path
from .views import CourseListCreateView, EnrollmentListCreateView, StudentListCreateView

urlpatterns = [
    path('api/courses/', CourseListCreateView.as_view(), name='course-list'),
    path('api/enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('api/students/', StudentListCreateView.as_view(), name='student-list'),
]