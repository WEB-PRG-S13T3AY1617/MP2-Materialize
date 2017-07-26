from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    degree_or_office = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='marketplace/static/marketplace/img/', blank=True, default='marketplace/static/marketplace/img/def/default.png')
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    CHOICES = (
        ('1', 'Academic'),
        ('2', 'Office'),
    )
    type = models.CharField(max_length=1, choices=CHOICES, default='')
    course = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
