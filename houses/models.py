from django.db import models

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140, null=True)
    price = models.PositiveIntegerField(null=True)
    description = models.TextField()
    address = models.CharField(max_length=140, null=True)
    smoking_allowed = models.BooleanField(default=True, null=True)
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL)
    def __str__(self):
        return self.name