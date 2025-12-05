from django.urls import path
from .views import CourseListCreateView, EnrollmentListCreateView, StudentListCreateView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('students/', StudentListCreateView.as_view(), name='student-list'),
]