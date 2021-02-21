from django.db import models
# Update the existing AbstractUser model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add age
    age = models.PositiveIntegerField(null = True, blank = True)
    #'null' implies database-related void value, 'blank' implies user choses to keep it empty
