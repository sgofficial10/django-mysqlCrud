from django.db import models

# Create your models here.
class Classes(models.Model):
    code = models.CharField(max_length=150)
    className = models.CharField(max_length=150)
    isDelete = models.CharField(max_length=10)


    class Meta:
        db_table = "schoolink_classes"
    