from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from taggit.managers import TaggableManager


degree_or_office = models.CharField(max_length=50)
degree_or_office.contribute_to_class(User, 'degree_or_office')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='marketplace/static/marketplace/img/', blank=True, default='marketplace/static/marketplace/img/def/default.png')
    name = models.CharField(max_length=25)
    condition = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    CHOICES = (
        ('Academic', 'Academic'),
        ('Office', 'Office'),
    )
    type = models.CharField(max_length=8, choices=CHOICES)
    course = models.CharField(max_length=20, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name
