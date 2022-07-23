from django.db import models
import uuid

# Create your models here.



class Package(models.Model):

    class StatusChoice(models.TextChoices):
        RECIEVED    = 'RE', ('Recieved')   #student revieved this package
        DELIVERED   = 'DE', ('Delivered')  #front dest recieved this package

    status = models.CharField(
        max_length  = 2,
        choices     = StatusChoice.choices,
        default     = StatusChoice.DELIVERED
    )
    description         = models.TextField(blank = False, null = False, default= '')
    package_ID          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracking_number     = models.TextField(blank = False, null = False, default= '')
    building    = models.TextField(max_length = 3, blank = False, null = True)
    weekday     = models.TextField(max_length = 3, blank = False, null = True)
    order       = models.IntegerField(null = True)

    carrier             = models.TextField(blank = False, null = False, default= '')
    pic                 = models.ImageField(upload_to ='uploads/', null=True)
    comment             = models.TextField(blank = False, null = False, default= '')
    date                = models.DateField(default=True, blank = False, null = False)
    reciever_initial    = models.TextField(max_length = 3, blank = False, null = False, default= '')

