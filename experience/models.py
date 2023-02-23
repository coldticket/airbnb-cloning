from django.db import models
from common.models import CommonModel
class Experience(CommonModel):
    """experience model definition """
    country = models.CharField(max_length=50,default="south korea")
    city = models.CharField(max_length=80, default="seoul")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=20)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experience.Perk")
    category = models.ForeignKey("category.Category",on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name
class Perk(CommonModel):
    """included expereicence"""
    name= models.CharField(max_length=100)
    detail = models.CharField(max_length=250, blank=True,null=True)
    explanation = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
