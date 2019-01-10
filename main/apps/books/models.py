from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploaded_books = models.ForeignKey(User, related_name='uploader')
    liked_books = models.ManyToManyField(User, related_name='liked_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
