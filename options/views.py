from tracking.models import Element, Categorie, Workingtime
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import Choicefrom, Categorieform, Elementform, Worktimefrom
import datetime
from django.contrib import messages
from django.db import IntegrityError

def load_elements(request):
    categories_id = request.GET.get('categories')
    element = Element.objects.filter(categories_id=categories_id).order_by('categories')
    return render(request, 'input_element_list_options.html',
                  {'element': element}
                  )

def options(request):

    choice_form = Choicefrom(request.POST)

    if request.method == 'POST':

        work_time_form = Worktimefrom(request.POST)

        if work_time_form.is_valid():
            work_time = work_time_form.cleaned_data['workingtime']

            try:
                Workingtime.objects.all().delete()

            except(IntegrityError, ValueError, TypeError):
                pass

            wkt = Workingtime(
                user_id=request.user,
                workingtime=work_time
            )

            wkt.save()


            messages.success(request, ' Erfolgreich gespeichert')

    else:
        work_time_form = Worktimefrom()

    return render(request,'options.html',
                  {
                      'choice_form': choice_form,
                      'work_time_form': work_time_form
                   })

def addcategories(request):
    if request.method == 'POST':
        categorieform = Categorieform(request.POST)
        if categorieform.is_valid():
            cat = categorieform.cleaned_data['cat']

            ca = Categorie(
                cat = cat
            )

            ca.save()

            messages.success(request, ' Erfolgreich gespeichert')

    return render(request, 'categorie_input.html',
                  {
                      'categorieform': Categorieform
                  })

def addelements(request):
    if request.method == 'POST':
        elementsform = Elementform(request.POST)
        if elementsform.is_valid():
            categories = elementsform.cleaned_data['categories']
            elements = elementsform.cleaned_data['element']
            ca = Element(
                categories = categories,
                element = elements
            )

            ca.save()

            messages.success(request, ' Erfolgreich gespeichert')

    return render(request, 'element_input.html',
                  {'elementsform': Elementform}
                  )

def addfavortites(request):

    if request.method == 'POST':

        favorites = request.POST['favorites']
        categorie = request.POST['categorie']
        favorites = favorites.split(",")[1:]
        print(categorie)
        print(favorites)


    return render(request, 'options.html')



















