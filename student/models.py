from django.db import models


# ======================
# STUDENT
# ======================
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.studentName


# ======================
# PRODUCT
# ======================
class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDesc = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20, null=True, blank=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.productName


# ======================
# STUDENT PROFILE
# ======================
class StudentProfile(models.Model):
    profileId = models.AutoField(primary_key=True)

    HOBBIES = (
        ("reading", "Reading"),
        ("writing", "Writing"),
        ("swimming", "Swimming"),
    )

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
    # studentImage = models.ImageField(upload_to="student/", null=True, blank=True)

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return f"{self.student.studentName}'s Profile"


# ======================
# CATEGORY
# ======================
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName


# ======================
# SERVICE
# ======================
class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.FloatField()
    serviceStatus = models.BooleanField(default=True)
    discount =models.FloatField(null=True)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        db_column="categoryId"
    )

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName
