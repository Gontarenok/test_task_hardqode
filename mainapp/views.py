from rest_framework.viewsets import ModelViewSet
from mainapp.models import User, Lesson
from mainapp.serializers import UserModelSerializer, LessonModelSerializer, ProductModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer

class ProductModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = ProductModelSerializer
