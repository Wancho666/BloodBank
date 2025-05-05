from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    # Linking the Donor model to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Profile picture for the donor
    profile_pic = models.ImageField(upload_to='profile_pic/Donor/', null=True, blank=True)

    # Blood group choices
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
    
    # Donor address and mobile fields
    address = models.CharField(max_length=255)  # Increased max_length for more flexibility
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.get_name  # Return the donor's full name as the string representation

class BloodDonate(models.Model):
    # ForeignKey to the Donor model
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    
    # Blood donation details
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()  # Age should be a positive integer
    bloodgroup = models.CharField(max_length=10)  # Blood group is stored for each donation
    unit = models.PositiveIntegerField(default=0)  # Number of blood units donated
    status = models.CharField(max_length=20, default="Pending")  # Status of donation (Pending, Approved, etc.)
    date = models.DateField(auto_now=True)  # Date of donation is auto-filled

    def __str__(self):
        return f"Donation by {self.donor.get_name} on {self.date}"  # Better representation of the donation
