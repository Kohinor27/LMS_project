from django.urls import path
from .views import CourseListCreateView, EnrollmentListCreateView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
]