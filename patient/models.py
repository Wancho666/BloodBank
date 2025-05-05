from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    # Linking the Patient model to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Profile picture for the patient
    profile_pic = models.ImageField(upload_to='profile_pic/Patient/', null=True, blank=True)

    # Age of the patient
    age = models.PositiveIntegerField()

    # Blood group (using choices for predefined values)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    # Blood group (now using choices for validation)
    bloodgroup = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    
    # Disease the patient is suffering from
    disease = models.CharField(max_length=100)
    
    # Doctor's name overseeing the patient's treatment
    doctorname = models.CharField(max_length=50)

    # Patient's address (increased max_length for flexibility)
    address = models.CharField(max_length=255)  # Increased max_length to allow more characters
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.get_name  # Better string representation for the Patient model
