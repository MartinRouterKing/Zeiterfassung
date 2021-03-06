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
    user = User.objects.all().order_by('username')
    cat = Categorie.objects.all().order_by('cat')
    wie = list(set(Element.objects.all().order_by('wie').values_list('wie', flat=True)))
    obj = list(set(Element.objects.all().order_by('obj').values_list('obj', flat=True)))
    
    

    return render(request, 'accounting/accounting.html',
                  {'form': user,
                   'categories': cat,
                   'wie': wie,
                   'obj': obj
                })

def ajaxpie(request):

    if request.method == 'POST':

        pie_data = 0

    return render(request, 'accounting/accounting_pie.html',
                  {'pie_data': pie_data}
                  )

def ajaxtable(request):
    print("ACTION")
    if request.method == "POST":

        '''
        Integrate the user choice field
        if nothing selected the empty list set to all users       
        '''

        user_name = request.POST.getlist("user[]")

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
        Get the value from the start and end date choice
        '''

        start_date = request.POST.getlist("start_date")[0]

        end_date = request.POST.getlist("end_date")[0]
        

        '''
        Get the Tracking data correspoonding on the user choice
        '''

        obj = CalendarEvent.objects.filter(user_id__username__in=user_name)

        '''
        Filter the data corresonding to the disired time
        '''

        if start_date and end_date:
            obj = obj.filter(start__year=start_date.split("-")[1], start__month__gte=start_date.split("-")[0])
            obj = obj.filter(end__year=end_date.split("-")[1], end__month__lte=end_date.split("-")[0])


        obj = obj.filter(type__in=cat_choice)

        '''
        Generate the data for the table
        '''
        import pandas as pd
        from django.db.models import Sum
        #calc = Calc_Choices.objects.all().values_list('calc', flat=True)

        agg = obj.values('user_id__username', 'title', 'calc', 'type').annotate(Sum('hours')).order_by(
            'user_id__username', 'title', 'type')


        agg_title = agg.values('user_id__username', 'title', 'type').annotate(Sum('hours')).order_by(
            'user_id__username', 'title', 'type')

        id = 1
        data = []

        '''
        Build a table with the following structure

        Name    Wie     Obj     element     hours_ges       hours_per_cost

        __

        -Names, element and hours_per_cost comes from calendar model
        -Wie and Obj from the Element model
        -hours_ges and hours_per_cost are aggregated from the calendar model 
        '''

        for row in agg:
            id = + 1
            print(row)
            agg_ges = agg_title.filter(user_id__username=row['user_id__username'], title=row["title"], type=row["type"]).first()
            print(agg_ges)


            ele_obj = Element.objects.filter(element__kat_element=row['title'], categories__cat=row["type"],
                                             obj__in=obj_choice, wie__in=wie_choice).first()

            if ele_obj == None:
                wie = None
                obj = None
            else:
                wie = ele_obj.wie
                obj = ele_obj.obj

            data_row = {'id': str(id), "Name": row['user_id__username'], 'Wie': wie, 'Objekt': obj,
                        'Typ': row['type'], 'Kategorie': row['title'], 'Gesamt': str(agg_ges['hours__sum'])}

            data_row.update({x['calc']: str(x['hours__sum']) for x in agg.filter(title=row["title"],
                                                                                 type=row["type"],
                                                                                 user_id__username=row['user_id__username'])})
            if data_row not in data:
                data.append(data_row)

        ges_sum = {}
        calc = []
        for d in data:
            for key, value in d.items():
                if key != 'Name' and key != 'Wie' and key != 'Objekt' and key != 'Typ' and key != 'id' and key != 'Kategorie':
                    calc.append(key)
                    print(key)
                    try:
                        ges_sum[key] = ges_sum[key] + float(value)
                    except (KeyError):
                        ges_sum[key] = 0 + float(value)
        print(ges_sum)
        data.append({**{'Name': '', 'Wie': '', 'Objekt': '', 'Typ': '', 'id': '', 'Kategorie': ''}, **ges_sum})
        calc = set(calc)
        print(calc)
        import django_tables2 as tables
        table = TrackingTable(data=data, template_name='django_tables2/bootstrap.html',
                              extra_columns=[(str(key), tables.Column()) for key in calc])

        RequestConfig(request).configure(table)
        from django_tables2.export.export import TableExport

        export_format = request.POST.get('_export', None)

        if TableExport.is_valid_format(export_format):
            exporter = TableExport('csv', table)
            return exporter.response('table.{}'.format('csv'))

        RequestConfig(request, paginate={'per_page': 50000}).configure(table)

        return render(request, 'accounting/table.html',
                      {
                          'table': table
                      })
