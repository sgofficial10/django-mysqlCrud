from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class User(models.Model):
    gcm_id = models.IntegerField()
    fname = models.CharField(max_length = 255)
    deviceType = models.CharField(max_length=150)
    active = models.IntegerField(default=0)
    userType = models.CharField(max_length=10)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rememberToken = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    isDelete = models.CharField(max_length=10)



    class Meta:
        db_table = "schoolink_user"
