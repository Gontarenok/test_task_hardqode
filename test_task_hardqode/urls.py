from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import UserModelViewSet, LessonModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('users_lessons', UserModelViewSet)
router.register('users_lessons_product', LessonModelViewSet)
router.register('product_statistics', ProductModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
