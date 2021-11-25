from django.db import models
from solo.models import SingletonModel

class Calendar(models.Model):

    name = models.CharField(max_length=200)

    # Example config:
    #{
    #   "weekdays": [
    #       "weekday1",
    #       "weekday2",
    #   ],
    #   "months": [
    #       {
    #           "name": "month1",
    #           "duration": 30
    #       },
    #       {
    #           "name": "month2",
    #           "duration": 30
    #       },
    #   ],
    #   "moons": [
    #       {
    #           "name": "moon1",
    #           "cycle": 30,
    #           "offset": 0
    #       },
    #       {
    #           "name": "moon2",
    #           "cycle": 30,
    #           "offset": 0
    #       },
    #   ],
    #   "holidays": [
    #       {
    #           "name": "holiday1",
    #           "description": "a holiday",
    #           "startdate": "01-01",
    #           "enddate": "01-01"
    #       },
    #       {
    #           "name": "holiday2",
    #           "description": "a holiday",
    #           "startdate": "01-01",
    #           "enddate": "01-01"
    #       },
    #   ],
    #}

    config = models.JSONField()

class CalendarConfig(SingletonModel):

    class Meta:
        verbose_name = "Calendar Config"

    activeCalendar = models.ForeignKey(Calendar, on_delete=models.SET_NULL, blank=True, null=True)
