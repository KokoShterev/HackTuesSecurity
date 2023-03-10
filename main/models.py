from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    website_password = models.CharField(max_length=1048)

    def __str__(self):
        return "user: " + self.user.username + "   " + "website: " + self.website
