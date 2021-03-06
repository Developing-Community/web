from django.db import models
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from enumfields import EnumField


class TaxonomyType(Enum):
    LEARNING_FIELD = "LEARNING_FIELD"
    SUBJECT = "SUBJECT"  # content subject


class Term(models.Model):
    title = models.CharField(max_length=255, unique=True)
    taxonomy_type = EnumField(TaxonomyType, default=TaxonomyType.SUBJECT, max_length=1000)

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


class TermRealtionType(Enum):  # A subclass of Enum
    CHILD_OF = "CHILD_OF"


class TermRelation(models.Model):
    content = models.ForeignKey(Term, related_name='source', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='destination', on_delete=models.CASCADE)
    type = EnumField(TermRealtionType, default=TermRealtionType.CHILD_OF, max_length=1000)
