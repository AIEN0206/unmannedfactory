from __future__ import unicode_literals
from django.db import models
from django.db import connection


class Drivelesscar(models.Model):
    id = models.IntegerField(primary_key=True)
    carid = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    battery = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'drivelesscar'

    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from drivelesscar")
            datas = cursor.fetchall()
        return datas


