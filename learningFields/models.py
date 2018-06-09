from django.db import models


# Create your models here.

class LearningField(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['title']

    def children(self):
        return LearningField.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
