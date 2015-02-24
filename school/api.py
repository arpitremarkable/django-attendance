from tastypie import fields
from tastypie.resources import ModelResource

from school import models

import datetime


class BehaviourResource(ModelResource):
    class Meta:
        queryset = models.Behaviour.objects.all()
        resource_name = 'behaviour'
        excludes = ['id']


class PointResource(ModelResource):
    behaviour = fields.ForeignKey(BehaviourResource, 'behaviour', full=True, null=True, blank=True)
    class Meta:
        queryset = models.Point.objects.all()
        resource_name = 'behaviour'
        fields = ['behaviour']


class AttendanceResource(ModelResource):
    point = fields.ToManyField(PointResource, 'point_set', full=True, null=True, blank=True)
    class Meta:
        queryset = models.Attendance.objects.all()
        resource_name = 'attendance'
        excludes = ['id']


def attendance_set(bundle):
    try:
        date = datetime.date(year=int(bundle.request.GET['year']), month=int(bundle.request.GET['month']), day=int(bundle.request.GET['day']))
    except (KeyError, ValueError) as e:
        date = datetime.date.today()
    return bundle.obj.attendance_set.filter(date=date)

class UserResource(ModelResource):

    attendances = fields.ToManyField(AttendanceResource, attendance_set, full=True, null=True, blank=True)
    class Meta:
        queryset = models.User.objects.all()
        resource_name = 'user'
        fields = ['first_name', 'last_name', 'username']
