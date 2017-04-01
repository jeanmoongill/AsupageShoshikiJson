from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'

class Soshiki(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'soshiki'



