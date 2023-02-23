from django.db import models
from common.models import CommonModel

class Category(CommonModel):
    """room or experience category"""
    class CategoryKindChoices(models.TextChoices):
        ROOM= ("room","Room")
        EXPERIENCE=("experience","Experience")
    name=models.CharField(max_length=50)
    kind=models.CharField(max_length=15,choices=CategoryKindChoices.choices)
    def __str__(self):
        return self.name
    class Meta:
          verbose_name_plural = "Categories"




