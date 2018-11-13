# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from tracking.models import Categorie


class CalendarEvent(models.Model):
    """The event set a record for an
    activity that will be scheduled at a
    specified date and time.

    It could be on a date and time
    to start and end, but can also be all day.

    :param title: Title of event
    :type title: str.

    :param start: Start date of event
    :type start: datetime.

    :param end: End date of event
    :type end: datetime.

    :param all_day: Define event for all day
    :type all_day: bool.
    """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.TextField(('Id'), blank=True, max_length=200)
    title = models.CharField(_('Title'), blank=True, max_length=200)
    type = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    start = models.DateTimeField(_('Start'))
    hours = models.IntegerField(('Workingtime'), blank=True)
    end = models.DateTimeField(_('End'))
    note = models.TextField(('Notiz'), blank=True, max_length=200)
    all_day = models.BooleanField(_('All day'), default=False)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')



    def __unicode__(self):
        return self.title

    def __str__(self):
        return '{},{},{},{}'.format(
            self.user_id,
            self.type,
            self.title,
            self.start,
            self.end,
            self.note,
            self.all_day)
