from django.db import models


class Shoshiki(models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shoshiki'


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'



