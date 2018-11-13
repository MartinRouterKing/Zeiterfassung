from django.shortcuts import render
from calender.models import CalendarEvent
from .tables import TrackingTable
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

def tracking(request):
    table = TrackingTable(CalendarEvent.objects.filter(user_id=request.user.id),template_name = 'django_tables2/bootstrap.html')

    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format('xlsx'))


    return render(request, 'list.html', {
        'table': table
    })

from tablib import Dataset
from .resources import TrackingRessource


def simple_upload(request):
    if request.method == 'POST':
        person_resource = TrackingRessource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
