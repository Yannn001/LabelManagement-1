from django.db import models
import uuid

# Create your models here.

class User(models.Model):

        class Role(models.TextChoices):
                RoleADMIN       = 'AD', ('Admin')   
                STAFF           = 'ST', ('Staff')  
                USER            = 'US', ('User') 

        role = models.CharField(
                max_length = 2,
                choices = Role.choices,
                default = Role.USER,
                null = True
                ) 
        user_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        first_name      = models.TextField(max_length = 20, blank = True, null = True)
        middle_name     = models.TextField(max_length = 20, blank = True, null = True)
        last_name       = models.TextField(max_length = 20, blank = True, null = True)
        password = models.TextField(blank = False, null = False, default= '')
        building = models.TextField(blank = False, null = False, default= '')
