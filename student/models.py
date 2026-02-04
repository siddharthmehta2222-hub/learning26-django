from django.db import models


class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"


class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDesc = models.TextField()
    productStock = models.PositiveIntegerField()
    productcolor = models.CharField(max_length=20, null=True)
    productstatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"
