from django.db import models

# Create your models here

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class CV(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=40)
    mob=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.TextField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    materials=models.CharField(max_length=100)

    def __str__(self):
        return self.name




