from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)

    first_name = models.CharField(max_length=150, blank=False)
    
    last_name = models.CharField(max_length=150, blank=False)

    email = models.EmailField(max_length=255, unique=True)
    
    phone_number = models.CharField(max_length=15, blank=False)  # Adjust length as needed

    age = models.IntegerField(default=18)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
