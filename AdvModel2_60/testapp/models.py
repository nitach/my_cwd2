from django.db import models

# Create your models here.
class BaseClass(models.Model):
    f1=models.CharField(max_length=30)
    f2=models.CharField(max_length=30)

class ChildClass1(BaseClass):
    f3=models.CharField(max_length=30)
    f4=models.CharField(max_length=30)
class ChildClass2(BaseClass):
    f5=models.IntegerField()
