from tracking.models import Categorie, Workingtime, Categorie, Element
from calender.models import CalendarEvent
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Sum


def ControllingView(request):
    userform = User.objects.all()
    catform = Categorie.objects.all()

    return render(request, 'controlling.html',
                  {'userform': userform,
                   'catform': catform}
                  )
def search(request):

    if request.method == 'POST':
        user_search = request.POST.getlist("search_user[]")
        cat_search = request.POST.getlist("search_cat[]")
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        percent = request.POST["percent"]
        from datetime import datetime

        start_date_iso = datetime.strptime(start_date + " +0000", '%m-%Y %z')
        start_date_iso.isoformat()

        end_date_iso = datetime.strptime(end_date + "+0000", '%m-%Y%z')
        end_date_iso.isoformat()

        import datetime
        import calendar

        def add_months(sourcedate, months):
            month = sourcedate.month - 1 + months
            year = sourcedate.year + month // 12
            month = month % 12 + 1

            day = min(sourcedate.day, calendar.monthrange(year, month)[1])

            return datetime.date(year, month, day)

        end_date_iso = add_months(end_date_iso,1)
        data = {}
        hours_list = []
        label_list = []
        colors = ['#1abc9c', '#34495e', '#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6',
                  "#bccad6", "#8d9db6", "#667292", "#f1e3dd", "#cfe0e8", "#b7d7e8", "#87bdd8", "#daebe8"]
        counter=0
        for i in cat_search:
            hours_list = []
            search_obj = CalendarEvent.objects.filter(user_id__username__in=user_search,
                                                      type=i,
                                                      start__range = [start_date_iso, end_date_iso]).aggregate(Sum('hours'))
            if search_obj['hours__sum'] is not None:
                hours_list.append(float(search_obj['hours__sum']))
            else:
                hours_list.append(0)

            if len(i) > 30:
                data[i[:30] + "..."] = []
                data[i[:30] + "..."].append(hours_list)
                data[i[:30] + "..."].append(colors[counter])

            else:
                data[i] = []
                data[i].append(hours_list)
                data[i].append(colors[counter])

            counter += 1

        if percent == 'true':
            hour_sum = 0
            data_new = data
            print(data_new)

            for key, values in data_new.items():
                hour_sum = hour_sum + values[0][0]
            print(hour_sum)
            for key, values in data_new.items():
                print(values)
                data[key][0]= [round((values[0][0]/hour_sum)*100, 2)]
        print(data)

    return render(request, 'controlling_load_pie.html',
                  {'label_list': label_list,
                   'data': data,
                   'hours_list': hours_list}
                  )

def search_line(request):

    if request.method == 'POST':
        user_search = request.POST.getlist("search_user[]")
        cat_search = request.POST.getlist("search_cat[]")
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        percent = request.POST["percent"]

        colors = ['#1abc9c', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6','#2ecc71',]
        month_labels = ['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez']

        def monthlist_fast(dates):
            start, end = [datetime.strptime(_, "%m-%Y") for _ in dates]
            total_months = lambda dt: dt.month + 12 * dt.year
            mlist = []
            month_numlist = []
            year_numlist = []
            for tot_m in range(total_months(start) - 1, total_months(end)):
                y, m = divmod(tot_m, 12)
                mlist.append(datetime(y, m + 1 , 1).strftime("%b-%y"))
                month_numlist.append(m+1)
                year_numlist.append(y)
            return mlist, month_numlist, year_numlist

        month_list, month_num, year_num = monthlist_fast([start_date, end_date])

        data = {}

        for user, color in zip(user_search, colors):
            data[user] = {}
            data[user]['hours'] = []
            data[user]['color'] = color
            for month, year in zip(month_num,year_num):
                search_obj = CalendarEvent.objects.filter(user_id__username=user,
                                                          type__in= cat_search,
                                                          start__month = month,
                                                          start__year = year,
                                                          end__year = year).aggregate(Sum('hours'))

                if search_obj['hours__sum'] is not None:
                    print(search_obj)
                    data[user]['hours'].append(float(search_obj['hours__sum']))
                else:
                    data[user]['hours'].append(0)
        print(data)
        print(month_list)
    return render(request, 'controlling_load_line.html',
                  {'data': data,
                   'month_list': month_list
                   }
                  )