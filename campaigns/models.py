from django.db import models
from team.models import Team
# Create your models here.


#Sales Campaign

class Product(models.Model):
    seller = models.ForeignKey(Team, on_delete=models.CASCADE, blank = True, related_name="seller")
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)