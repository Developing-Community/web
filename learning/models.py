from django.db import models

from taxonomy.models import Term
from web import settings


class MentoringInfo(models.Model):
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    mentoring_field = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='mentoring_field')
    road_map = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.mentor.username + " | " + self.mentoring_field.title


class LearningInfo(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    learning_field = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='learning_field')

    def __str__(self):
        return self.mentor.username + " | " + self.mentoring_field.title

class Mentoring(models.Model):
    student_info = models.ForeignKey(LearningInfo, null= False, blank= False, related_name="student_info", on_delete=models.CASCADE)
    mentor_info = models.ForeignKey(LearningInfo, null= False, blank= False, related_name="mentor_info", on_delete=models.CASCADE)

    def __str__(self):
        return self.student_info.student.username + " | " + self.mentor_info.mentor.username + " | " + self.mentor_info.mentoring_field.title


class QualificationInfo(models.Model):
    qualified_student_info = models.ForeignKey(LearningInfo, null=False, blank=False, related_name="qualified_student_info", on_delete=models.CASCADE)
    qualifier = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.student.username + " | " + self.qualifier.name + " | " + self.learning_field.title + " | " + str(self.score)


#TODO: Add model for requests - mentoring request, etc,...