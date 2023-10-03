from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""В этом задании у нас есть три бизнес-задачи на хранение:
1. Создать сущность продукта. У продукта должен быть владелец. 
Необходимо добавить сущность для сохранения доступов к продукту для 
пользователя.
2. Создать сущность урока. Урок может находиться в нескольких продуктах 
одновременно. В уроке должна быть базовая информация: название, 
ссылка на видео, длительность просмотра (в секундах).
3. Урок могут просматривать множество пользователей. 
Необходимо для каждого фиксировать время просмотра и фиксировать 
статус “Просмотрено”/”Не просмотрено”. 
Статус “Просмотрено” проставляется, если пользователь просмотрел 80% 
ролика.
"""


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    deleted = models.BooleanField(default=False, verbose_name="Удален")

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Product(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)

    def __str__(self):
        return f"#{self.pk} {self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class ProductAccess(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.user} {self.product}"

    class Meta:
        verbose_name = 'доступ'
        verbose_name_plural = 'доступы'


class Lesson(BaseModel):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class LessonView(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.IntegerField()  # Время просмотра в секундах
    status = models.CharField(max_length=10, choices=[
        ('VIEWED', 'Просмотрено'),
        ('NOT_VIEWED', 'Не просмотрено')
    ])

    def save(self, *args, **kwargs):
        # При сохранении проверяем, достиг ли пользователь 80% просмотра видео
        if self.viewed_time >= (0.8 * self.lesson.duration):
            self.status = 'VIEWED'
        else:
            self.status = 'NOT_VIEWED'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} ({self.lesson})"
