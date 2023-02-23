from django.db import models

class CommonModel(models.Model):
    """common model definiton"""

    created_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now=True,null=True)
    class Meta:
        abstract = True