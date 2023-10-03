from rest_framework.serializers import ModelSerializer
from mainapp.models import User, Lesson, Product


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'