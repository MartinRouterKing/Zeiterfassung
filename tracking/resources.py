from import_export import resources
from .models import Tracking


class TrackingRessource(resources.ModelResource):
    class Meta:
        model = Tracking
        fields = ('user_id', 'date', 'hours')
