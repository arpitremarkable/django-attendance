from django.contrib.auth.models import User
from django.db import models

from djangotoolbox.fields import ListField


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True, auto_now=True)
    time = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.date)

    class Meta:
        unique_together = ("user", "date", )


class Behaviour(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.IntegerField(verbose_name='point')

    def __unicode__(self):
        return "%s - %s" % (self.name, self.value)


class Point(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.PROTECT)
    behaviour = models.ForeignKey(Behaviour, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return "%s - %s" % (self.attendance, self.behaviour)
