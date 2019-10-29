from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
# Create your models here.

class SoftDeletionQuerySet(QuerySet):

    def delete(self):
        for obj in self:
            obj.deleted_on = timezone.now()
            obj.save()

    def undelete(self):
        for obj in self:
            obj.deleted_on=None
            obj.save()

class SoftDeletionManager(models.Manager):

    def get_query(self):
        return SoftDeletionQuerySet(self.model, using = self._db).filter(deleted_on_isnull=True)





class SoftDeletionModel(models.Model):
    class Meta:
        abstract = True

    deleted_on = models.DateTimeField(null=True, blank=True)
    objects = SoftDeletionManager()
    originals_object = models.Manager()

    def delete(self):
        self.deleted_on = timezone.now()
        self.save()

    def undelete(self):
        self.deleted_on=None
        self.save()

class Classes(SoftDeletionModel):
    code = models.CharField(max_length=150)
    className = models.CharField(max_length=150)
    isDelete = models.CharField(max_length=10)


    class Meta:
        db_table = "schoolink_classes"



class Sections(SoftDeletionModel):
    code = models.CharField(max_length=150)
    classes = models.ForeignKey(Classes,  on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)


    class Meta:
        db_table = "schoolink_sections"
    