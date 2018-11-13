from import_export import resources
from calender.models import CalendarEvent


class TrackingRessource(resources.ModelResource):
    class Meta:
        model = CalendarEvent
        fields = ('user_id', 'title', 'type', 'start', 'end', 'note')
