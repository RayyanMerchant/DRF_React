from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Calc(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    newid = models.IntegerField()
    result = models.IntegerField()
    def __str__(self):
        return str(self.num1) + " + " + str(self.num2)

