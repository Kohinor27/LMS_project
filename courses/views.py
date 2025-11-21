from rest_framework import generics
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer

# List all courses OR create a new course
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# List all enrollments OR create a new enrollment
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
