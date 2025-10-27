from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return self.name


class Marker(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    lat = models.FloatField()
    lng = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='markers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='markers')

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.created_by.username} - {self.date}'
    
    class Meta:
        ordering = ['-date']


