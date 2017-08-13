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


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    CHOICES = (
        ('Exchange', 'Exchange'),
        ('Purchase', 'Purchase'),
    )
    type = models.CharField(max_length=8, choices=CHOICES)
    amount = models.DecimalField(decimal_places=2, blank=True, max_digits=20, null=True)
    secondhand = models.ForeignKey(Post, null=True, blank=True, related_name='secondhand')

    def __str__(self):
        return self.post.name
