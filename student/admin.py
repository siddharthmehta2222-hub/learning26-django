from django.contrib import admin
from .models import Student, Product, StudentProfile,Category,Service,Department, Task,Project, Employee, Client, ClientProfile


# Register your models here.
admin.site.register(Student)            
admin.site.register(Product)   
admin.site.register(Category)
admin.site.register(Service)    
admin.site.register(StudentProfile) 
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Client)
admin.site.register(ClientProfile)


