import django_tables2 as tables
from tracking.models import Tracking

class TrackingTable(tables.Table):
    Wie = tables.Column()
    Objekt = tables.Column()
    Kategorie = tables.Column()
    Gesamt = tables.Column()




