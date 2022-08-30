from django.db import models

# Create your models here.

        
class Department(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    class Meta:
        db_table ='Department'
            