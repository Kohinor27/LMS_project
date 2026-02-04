from django.urls import path
from .views import (
    CourseListCreateView,
    EnrollmentListCreateView,
    StudentListCreateView,
    CourseDetailView,
    StudentDetailView,
    login_view,
)

urlpatterns = [
    # Courses
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    #Enrollments
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),

    # Students
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    # Login
    path('login/', login_view, name='login'),
]