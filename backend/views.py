from .models import *
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class StudentViewsets(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



































































# def home(request):
    
#     #students = Student.object.all()
#     #list(students = Student.object.value())
    
#     students = []
#     for student in Student.objects.all():
#         students.append({
            
#             'name' :student.name,
#             'course' :student.course,
#             'rating' :student.rating,                   
#         }                         
#         )
    
#     return JsonResponse(students, safe=False)