from django.shortcuts import render
from django.contrib.auth.models import User
from tracking.models import Categorie, Element, Calc_Choices
from django_tables2.config import RequestConfig
from .tables import TrackingTable
from calender.models import CalendarEvent




def accounting(request):

    '''
    Get date for choices from the models.

    If a choice field is changing, a ajax function will
    rendering the table with the given data choices.
    '''
    user = User.objects.all()
    cat = Categorie.objects.all()
    wie = list(set(Element.objects.all().values_list('wie', flat=True)))
    obj = list(set(Element.objects.all().values_list('obj', flat=True)))

    print(obj)
    return render(request, 'accounting.html',
                  {'form': user,
                   'categories': cat,
                   'wie': wie,
                   'obj': obj
                })

def ajaxpie(request):

    if request.method == 'POST':

        pie_data = 0

    return render(request, 'accounting_pie.html',
                  {'pie_data': pie_data}
                  )

def ajaxtable(request):

    if request.method == "POST":

        '''
        Integrate the user choice field
        if nothing selected the empty list set to all users       
        '''
        user_name = request.POST.getlist("user")

        if user_name==[] or user_name[0]=='--Alle--' :
            user_name = '--Alle--'
        else:
            user_name = user_name[0]

        '''
        Get the value from the categorie choice
        '''
        cat_choice = request.POST.getlist("ca[]")

        '''
        Get the value from the Wie choice
        '''
        wie_choice = request.POST.getlist("wie[]")

        '''
        Get the value from the Wie choice
        '''
        obj_choice = request.POST.getlist("obj[]")

        '''
        Get the elements for the selected categories and 
        delete double elements     
        '''
        elements = list(set(Element.objects.filter(categories__cat__in= cat_choice, wie__in=wie_choice, obj__in=obj_choice).values_list('element__kat_element', flat= True)))

        '''
        Get the Tracking data correspoonding on the user choice
        '''
        if user_name== '--Alle--':
            obj = CalendarEvent.objects.all()

        else:
            obj = CalendarEvent.objects.filter(user_id__username=user_name)


        '''
        Generate the data for the table
        '''
        from django.db.models import Sum
        calc = Calc_Choices.objects.all().values_list('calc',flat=True)
        print(calc)

        id = 1
        data = []
        calulate = {}
        for ele in elements:
            t = obj.filter(title=ele, type__in=cat_choice).aggregate(Sum('hours'))
            if t['hours__sum'] is None:
                calulate['Gesamt'] = 0
            else:
                calulate['Gesamt'] = t['hours__sum']

            for cal in calc:
                print(cal)
                c = obj.filter(title=ele, type__in=cat_choice, calc=cal).aggregate(Sum('hours'))
                print(c)
                if c['hours__sum'] is None:
                    calulate[cal] = 0
                else:
                    calulate[cal] = c['hours__sum']

            ele_obj = Element.objects.filter(element__kat_element=ele).first()

            data.append({**{'Wie': ele_obj.wie, 'Objekt': ele_obj.obj, 'id': id, 'Kategorie': ele}, **calulate})

        ges_sum = {}
        for d in data:
            for key, value in d.items():
                if key != 'Wie' and key != 'Objekt' and key != 'id' and key != 'Kategorie':
                    try:
                        ges_sum[key] = ges_sum[key]  + float(value)
                    except (KeyError):
                        ges_sum[key] = 0 + float(value)


        print(ges_sum)


        data.append({**{'Wie': '', 'Objekt': '', 'id': '', 'Kategorie': 'Gesamtsumme:'}, **ges_sum})


        import django_tables2 as tables
        table = TrackingTable(data=data,template_name='django_tables2/bootstrap.html', extra_columns=[(str(key), tables.Column()) for key in calc])

        RequestConfig(request).configure(table)
        from django_tables2.export.export import TableExport

        export_format = request.POST.get('_export', None)
        print(export_format)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport('csv', table)
            print(exporter.response('table.{}'.format('csv')))
            return exporter.response('table.{}'.format('csv'))

        RequestConfig(request, paginate={'per_page': 150}).configure(table)

        return render(request, 'table.html',
                          {
                              'table': table
                           })

