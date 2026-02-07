from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = "test_student"

    def __str__(self):
        return self.studentName
class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDesc = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20, null=True, blank=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "test_product"

    def __str__(self):
        return self.productName
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "test_category"

    def __str__(self):
        return self.categoryName
class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.FloatField()
    serviceStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "test_service"

    def __str__(self):
        return self.serviceName
HOBBIES = (
    ("reading", "Reading"),
    ("sports", "Sports"),
    ("music", "Music"),
)

class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        db_column="studentId"
    )
    studentHobbies = models.CharField(max_length=50, choices=HOBBIES)
    studentPhone = models.CharField(max_length=15)
    studentAddress = models.CharField(max_length=255)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table = "test_studentprofile"

    def __str__(self):
        return f"{self.student.studentName} Profile"
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Project(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)

    def __str__(self):
        return self.task_name
class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class ClientProfile(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.client.name

