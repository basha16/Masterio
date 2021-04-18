from django.db import models

# Create your models here.
class Member(models.Model):
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=12)


    def __str__(self):
        return self.Username

class Staffs_data(models.Model):
    Name= models.CharField(max_length=20)
    Email= models.CharField(max_length=40)
    Password= models.CharField(max_length=20)
    ConfirmPassword= models.CharField(max_length=16)

    def __str__(self):
        return self.Name