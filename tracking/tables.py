import django_tables2 as tables
from calender.models import CalendarEvent

class TrackingTable(tables.Table):

    user_id = tables.Column(verbose_name='Name')
    start = tables.DateTimeColumn(verbose_name='Start', format='d.m.Y, H:i')
    end = tables.DateTimeColumn(verbose_name='Ende', format='d.m.Y, H:i')
    hours = tables.Column(verbose_name='Stunden')
    title = tables.Column(verbose_name='Kategorie')
    type = tables.Column(verbose_name='Typ')
    note = tables.Column(verbose_name='Notiz')

    class Meta:
        model = CalendarEvent

        fields=[
                'id',
                'user_id',
                'start',
                'end',
                'hours',
                'title',
                'type',
                'note']

        attrs = {'class': 'table table-hover table-dark'}



