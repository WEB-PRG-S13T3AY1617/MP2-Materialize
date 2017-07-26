from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     username = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     degree_or_office = models.CharField(max_length=50, blank=True)
#
#     def __str__(self):
#         return self.username

degree_or_office = models.CharField(max_length=50)
degree_or_office.contribute_to_class(User, 'degree_or_office')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='marketplace/static/marketplace/img/', blank=True, default='marketplace/static/marketplace/img/def/default.png')
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    CHOICES = (
        ('Academic', 'Academic'),
        ('Office', 'Office'),
    )
    type = models.CharField(max_length=8, choices=CHOICES, default='')
    course = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
