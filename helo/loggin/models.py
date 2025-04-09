from django.db import models

class User(models.Model):
    ROLE_CHOICES = [('Employee', 'Employee'), ('Candidate', 'Candidate'), ('Examiner', 'Examiner'), ('Admin', 'Admin'), ('SME', 'SME')]
    DEPT_CHOICES = [('Tech', 'Tech'), ('Quality Check', 'Quality Check'), ('Media', 'Media'), ('Business Development', 'Business Development')]
    DESIGNATION_CHOICES = [('Developer', 'Developer'), ('Analyzer', 'Analyzer'), ('Business Development Executive', 'Business Development Executive')]

    user_role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    user_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPT_CHOICES)
    email_id = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    mobile_number = models.CharField(max_length=15)
    remarks1 = models.CharField(max_length=255, blank=True, null=True)
    remarks2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user_name
