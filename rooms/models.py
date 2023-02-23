from django.db import models
from common.models import CommonModel
class Room(CommonModel):
    """room definition description"""
    class RoomKindaChoices(models.TextChoices):
        ENTIRE_PLACE= ("entire_place", "Entire place")
        PRIVATE_ROOM= ("private_room", "Private room")
        SHARED_ROOM = ("Shaerd_room", "Shared room")
    name =models.CharField(max_length=180,default="")
    country = models.CharField(max_length=50,default="south korea")
    city = models.CharField(max_length=80, default="seoul")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets= models.PositiveIntegerField()
    descriptions= models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly= models.BooleanField(default= True)
    kind = models.CharField(max_length=20,choices=RoomKindaChoices.choices)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amaenities = models.ManyToManyField("rooms.Amenity")
    category = models.ForeignKey("category.Category",on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name
    
class Amenity(CommonModel):
    """amenity definition"""
    name= models.CharField(max_length=150,)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Amenities "
