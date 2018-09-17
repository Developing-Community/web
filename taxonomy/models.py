from enum import Enum
from django.db import models


class TaxonomyType(Enum):
    LEARNING_FIELD = "learning_field"
    SUBJECT = "subject"  # content subject


class Term(models.Model):
    title = models.CharField(max_length=255)
    title_fa = models.CharField(max_length=255,blank=True, null=True)
    taxonomy_type = models.CharField(
        max_length=30,
        choices=[(tag.value, tag.name) for tag in TaxonomyType],
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

    def __str__(self):
        return self.title

class TermRealtionType(Enum):   # A subclass of Enum
    CHILD_OF = "child_of"

class TermRelation(models.Model):
    source = models.ForeignKey(Term, related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey(Term, related_name='destination', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=30,
        choices=[(tag.value, tag.name) for tag in TermRealtionType]
    )