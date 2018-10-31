from django.views.generic import TemplateView
from django.contrib.auth.models import User
from tracking.models import Tracking, Categorie, Workingtime
import arrow
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import Choice
from datetime import datetime

def Analyticsview(request):

    '''
    Get the contractual working time per month from database
    '''

    working_time = Workingtime.objects.filter(user_id=request.user.id)
    working_time = int(working_time.values_list('time')[0][0] *4.35)

    '''
    Calculation the current month for further calculations
    '''
    currentmonth = datetime.now().month
    print(currentmonth)

    '''
    Get the working data from the database and calculation of the 
    workingtime per month.
    
        obj             -> working data objects
        obj_data        -> working date 
        obj_hours       -> working hours
        obj_categories  -> categories of the working activity
    '''
    obj = Tracking.objects.filter(user_id=request.user.id)
    obj_date = obj.values_list('date')
    obj_hours = obj.values_list('hours')
    obj_categories = obj.values_list('categories')
    list_hours = []

    for i in range(1, 13):
        a = 0
        for date, hour in zip(obj_date, obj_hours):
            if i == date[0].month:
                a = a + hour[0].hour
        list_hours.append(a)


    '''
    Calculation working time per month in percent
    '''
    working_time_perc = int(list_hours[currentmonth-2]/working_time *100)
    print(working_time_perc)

    '''
    Calculation overtime for the current month.
    '''
    print(list_hours[currentmonth-2])
    if working_time < list_hours[currentmonth-2]:
      overtime = (list_hours[currentmonth]-working_time)/100
    else:
        overtime = 0


    '''
    calculation of the working hours per categorie for the last 
    3 month
    '''

    list_cat = []
    list_cat_label= []

    for oe in list(set(obj_categories)):
        caz = Categorie.objects.filter(pk=oe[0])
        list_cat_label.append(str(caz[0]))


    for i in range(len(list_cat_label)):
        list_cat_label[i] = list_cat_label[i][:10]


    for c in range(1,len(list_cat_label)+1):

        h = 0
        for hour, cat in zip(obj_hours, obj_categories):

            if cat[0] == c:
                h = h + (hour[0].hour / sum(list_hours))*100
                h = round(h, 2)
        list_cat.append(h)



    #(obj_list.aggregate(Sum('hours')))
    # sum all hours per month in Querry


    # variable Data
    # Year = current Year or request year from form
    # month = current month or request month


    if request.method =='GET':
        choice = request.GET.get('options')

    return render(request, 'home.html',{
        'list_hours': list_hours,
        'list_cat_label': list_cat_label,
        'list_cat': list_cat,
        'choice': choice,
        'working_time_prec': working_time_perc,
        'overtime': overtime,
    })

"""

TODO: 
        - labels ausbessern, akktuell sind labels in html harcodes
        - 
"""