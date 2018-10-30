import django_tables2 as tables
from .models import Tracking

class TrackingTable(tables.Table):

    start_time = tables.TimeColumn(format='G:i:s')
    end_time = tables.TimeColumn(format='G:i:s')
    hours =tables.TimeColumn(format='H:i')
    categories = tables.Column()
    element = tables.Column()

    class Meta:
        model = Tracking

        fields=['id',
                'user_id',
                'date',
                'start_time',
                'end_time',
                'hours',
                'categories',
                'element',
                'notiz']

        attrs = {'class': 'table table-hover'}



