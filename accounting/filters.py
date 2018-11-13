from tracking.models import Tracking
import django_filters




class TrackingFilter(django_filters.FilterSet):
    class Meta:
        model = Tracking
        fields = ['user_id',
                    'date',
                    'start_time',
                    'end_time',
                    'hours',
                    'categories',
                    'element']