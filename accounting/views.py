from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User
from tracking.models import Categorie, Element, Tracking
from django_tables2.config import RequestConfig
from .tables import TrackingTable
from django_tables2.export.export import TableExport

from .filters import TrackingFilter


def accounting(request):

    '''
    Get date for choices from the models.

    If a choice field is changing, a ajax function will
    rendering the table with the given data choices.
    '''
    user = User.objects.all()
    cat = Categorie.objects.all()

    return render(request, 'accounting.html',
                  {'form': user,
                   'categories': cat,
                })



def ajaxtable(request):

    user = User.objects.all()
    cat = Categorie.objects.all()

    if request.method == "POST":

        '''
        Integrate the user choice field
        if nothing selected the empty list set to all users       
        '''
        user_name = request.POST.getlist("user")
        print(user_name)

        if user_name==[] or user_name[0]=='--Alle--' :
            user_name = '--Alle--'
        else:
            user_name = user_name[0]

        '''
        Get the value from the categorie choice
        '''
        cat_choice = request.POST.getlist("ca[]")
        print(cat_choice)

        '''
        Get the elements for the selected categories and 
        delete double elements     
        '''
        elements = list(set(Element.objects.filter(categories__cat__in= cat_choice).values_list('element', flat= True)))

        '''
        Get the Tracking data correspoonding on the user choice
        '''
        if user_name== '--Alle--':
            obj = Tracking.objects.all()

        else:
            obj = Tracking.objects.filter(user_id__username=user_name)


        '''
        Generate the data for the table
        '''
        from django.db.models import Sum


        id = 1
        data = []
        for ele in elements:
            t = obj.filter(element__element=ele).aggregate(Sum('hours'))

            data.append({'id': id, 'Kategorie': ele, 'Gesamt': t['hours__sum']})
            id = id + 1


        table = TrackingTable(data, template_name='django_tables2/bootstrap.html')
        RequestConfig(request, paginate={'per_page': 150}).configure(table)

        return render(request, 'table.html',
                          {
                              'table': table
                           })

