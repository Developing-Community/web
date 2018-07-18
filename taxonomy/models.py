from enum import Enum
from django.db import models


class TaxonomyType(Enum):
    LEARNING_FIELD = "learning_field"
    SUBJECT = "subject"  # content subject


class Term(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    title_fa = models.CharField(max_length=255)
    taxonomy_type = models.CharField(
        max_length=30,
        choices=[(tag, tag.value) for tag in TaxonomyType],
        default=TaxonomyType.SUBJECT
    )

    class Meta:
        ordering = ['title']

    def children(self):
        return Term.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
