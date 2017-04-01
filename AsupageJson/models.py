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


class TitleInfo(models.Model):
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'title_info'


class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    soshiki = models.ForeignKey(Soshiki, models.DO_NOTHING, db_column='soshiki')
    salary = models.TextField(blank=True, null=True)
    title = models.ForeignKey(TitleInfo, models.DO_NOTHING, db_column='title')
    create_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'



