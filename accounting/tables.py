import django_tables2 as tables

class TrackingTable(tables.Table):
    
    Name = tables.Column()
    Wie = tables.Column()
    Objekt = tables.Column()
    Typ = tables.Column()
    Kategorie = tables.Column()
    Gesamt = tables.Column()





