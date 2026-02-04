from rest_framework import generics
from .models import Course, Enrollment, Student
from .serializers import CourseSerializer, EnrollmentSerializer, StudentSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .permissions import IsTeacher, IsStudent, ReadOnly, IsAdmin
from rest_framework.permissions import IsAuthenticated


# List all courses OR create a new course
class EnrollmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admins & teachers see all enrollments
        if user.groups.filter(name__in=["admin", "Teacher"]).exists():
            return Enrollment.objects.all()

        # Students only see their own enrollments
        return Enrollment.objects.filter(student=user)



# List all students OR create a new student
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin)]

# Create a student

# View, update, or delete ONE course
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin | ReadOnly)]

# View, update, or delete ONE enrollment
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin | ReadOnly)]

# View, update, or delets ONE student
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin | ReadOnly)]

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=400)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key,
        'username': user.username,
        'groups': [group.name for group in user.groups.all()],
        'is_staff': user.is_staff,
        'is_superuser': user.is_superuser,
    })


