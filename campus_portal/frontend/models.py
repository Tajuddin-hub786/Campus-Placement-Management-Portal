from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)

    def _str_(self):
        return self.full_name
    

class Drive(models.Model):
    company_name = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=255)
    eligible_branches = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50) # Internship or Full Time
    job_role = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    process = models.TextField()
    last_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.company_name

class Application(models.Model):
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, related_name='apps')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    reg_no = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    btech_percent = models.FloatField()
    inter_percent = models.FloatField()
    ssc_percent = models.FloatField()
    resume = models.FileField(upload_to='resumes/')
    profile_image = models.ImageField(upload_to='profile_pics/')
    applied_at = models.DateTimeField(auto_now_add=True)



class SelectedStudent(models.Model):
    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    package = models.CharField(max_length=20)
    student_photo = models.ImageField(upload_to="selected_students/")

    def _str_(self):
        return self.student_name