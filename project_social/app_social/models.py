from django.db import models

# Create your models here.

class UserRegister(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 10)
    username = models.CharField(max_length = 13)
    address = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

