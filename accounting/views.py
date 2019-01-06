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
    print(wie)
    return render(request, 'accounting.html',
                  {'form': user,
                   'categories': cat,
                   'wie': wie
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
        Get the elements for the selected categories and 
        delete double elements     
        '''
        elements = list(set(Element.objects.filter(categories__cat__in= cat_choice, wie__in=wie_choice).values_list('element__kat_element', flat= True)))

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
        for ele in elements:
            t = obj.filter(title=ele, type__in=cat_choice).aggregate(Sum('hours'))
            ele_obj = Element.objects.filter(element__kat_element=ele).first()

            data.append({'Wie': ele_obj.wie, 'Objekt': ele_obj.obj, 'id': id, 'Kategorie': ele, 'Gesamt': t['hours__sum']})

            for key in calc:
                data[len(data)-1][key] = ""


            id = id + 1

        ges_sum = 0
        for d in data:
            if d['Gesamt'] is not None:
                ges_sum = ges_sum + float(d['Gesamt'])

        data.append({'Wie': '', 'Objekt': '', 'id': '', 'Kategorie': 'Gesamtsumme:', 'Gesamt': ges_sum})


        import django_tables2 as tables
        table = TrackingTable(data=data,template_name='django_tables2/bootstrap.html', extra_columns=[(str(key), tables.Column()) for key in calc])

        RequestConfig(request, paginate={'per_page': 150}).configure(table)

        return render(request, 'table.html',
                          {
                              'table': table
                           })

