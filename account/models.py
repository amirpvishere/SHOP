from django.db import models


class Account(models.Model):
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="img/User_Default.jpg")

    def __str__(self):
        return self.full_name
