from tracking.models import Element, Categorie, Workingtime, FavoriteElement, ElementTOKat
from tracking.models import KategorieElement, Kategorie, Calc_Choices
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import Choicefrom, Categorieform, editcatform, Worktimefrom, \
    editcatchoiceform, CalcForm, calcchoiceform,Elementform, editelechoiceform, MyRegistrationForm
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm


def load_elements(request):
    categories_id = request.GET.get('categories')
    user_id = User.objects.get(id=request.user.id)
    favorites = FavoriteElement.objects.filter(user_id = user_id,fav_element__categories_id=categories_id).values_list('fav_element__element', flat=True)
    element = Element.objects.filter(categories_id=categories_id).order_by('categories').exclude(element__in=favorites)

    return render(request, 'input_element_list_options.html',
                  {'element': element}
                  )

def load_favorites(request):
    categories_id = request.GET.get('categories')
    user_id = User.objects.get(id=request.user.id)
    favorites = FavoriteElement.objects.filter(user_id=user_id, fav_element__categories_id=categories_id).values_list('fav_element__element__kat_element', flat=True)

    return render(request, 'load_favorites.html',
                  {'favorites': favorites}
                  )

def options(request):
    choice_form = Choicefrom(request.POST)


    return render(request,'options.html',
                  {
                      'choice_form': choice_form,

                   })

def create_user(request):


    if request.method == 'POST':
        user = MyRegistrationForm(request.POST)
        print(user)
        print('valid_test')
        if user.is_valid():
            print("valid")
            email = user.cleaned_data['email']
            username = user.cleaned_data['username']
            first_name = user.cleaned_data['first_name']
            last_name = user.cleaned_data['last_name']
            is_superuser = user.cleaned_data['is_superuser']

            print(email)
            print(username)
            print(first_name)
            print(last_name)
            print(is_superuser)

            messages.success(request, 'Account created successfully')
        else:
            print("not valid")

    return render(request, 'admin_options.html', {})


def addcategories(request):

    '''
    Add a new categorie the the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: categorie (TextField)
    :return: save the Text input to the Database
    '''

    if request.method == 'POST':
        categorieform = Categorieform(request.POST)
        if categorieform.is_valid():
            cat = categorieform.cleaned_data['kategorie']

            ca = Kategorie(
                kategorie = cat
            )

            ca.save()

            messages.success(request, ' Erfolgreich gespeichert')

        else:
            messages.warning(request, ' Bitte Überprüfen Sie die Eingabe')

    return render(request, 'addcategories.html',
                  {'categorieform': Categorieform}
                  )

def editcategories(request):
    '''
    Edit the categories in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice and editform
    :return: Uppdate the selected choice in the model
    '''

    choice = editcatchoiceform()
    editform = editcatform()

    if request.method == 'POST':
        form = editcatform(request.POST)
        choice = editcatchoiceform(request.POST)
        if form.is_valid() and choice.is_valid():
            txt = form.cleaned_data['kategorie']
            edit = choice.cleaned_data['choice']
            q = Kategorie.objects.get(kategorie=edit)
            q. kategorie= txt
            q.save()
            messages.success(request, ' Erfolgreich gespeichert')
        else:
            messages.warning(request, ' Bitte Überprüfen Sie die Eingabe')

    return render(request, 'editcategories.html',
                  {'choice': choice,
                   'editform': editform}
                  )


def deletecategories(request):

    '''
    Delete elements in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice
    :return: Delete the selected categorie
    '''

    choice = editcatchoiceform()

    if request.method == 'POST':
        choice = editcatchoiceform(request.POST)
        if choice.is_valid():
            edit = choice.cleaned_data['choice']
            Kategorie.objects.filter(kategorie=edit).delete()
            messages.success(request, ' Erfolgreich Gelöscht')

    return render(request, 'deletecategories.html',
                  {'choice': choice}
                  )


def addelements(request):
    if request.method == 'POST':
        elementsform = Elementform(request.POST)
        if elementsform.is_valid():
            elements = elementsform.cleaned_data['kat_element']
            ca = KategorieElement(
                kat_element = elements
            )

            ca.save()

            messages.success(request, ' Erfolgreich gespeichert')

    return render(request, 'addelements.html',
                  {'elementsform': Elementform}
                  )

def editelements(request):
    '''
    Edit the elements in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice and editform
    :return: Uppdate the selected choice in the model
    '''

    choice = editelechoiceform()
    editform = Elementform()

    if request.method == 'POST':
        form = Elementform(request.POST)
        choice = editelechoiceform(request.POST)
        if form.is_valid() and choice.is_valid():
            txt = form.cleaned_data['kat_element']
            edit = choice.cleaned_data['choice']
            q = KategorieElement.objects.get(kat_element=edit)
            print(q)
            q.kat_element = txt
            q.save()
            messages.success(request, ' Erfolgreich gespeichert')
        else:
            messages.warning(request, ' Bitte Überprüfen Sie die Eingabe')

    return render(request, 'editelements.html',
                  {'choice': choice,
                   'editform': editform}
                  )
def deleteelements(request):

    '''
    Delete elements in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice
    :return: Delete the selected elements
    '''

    choice = editelechoiceform()


    if request.method == 'POST':
        choice = editelechoiceform(request.POST)
        if choice.is_valid():
            edit = choice.cleaned_data['choice']
            KategorieElement.objects.filter(kat_element=edit).delete()
            messages.success(request, ' Erfolgreich Gelöscht')

    return render(request, 'deleteelements.html',
                  {'choice': choice}
                  )
def addfavortites(request):

    if request.method == 'POST':

        favorites = request.POST['favorites']
        categorie = request.POST['categorie']
        favorites = favorites.split(",")[1:]
        print(favorites)
        FavoriteElement.objects.filter(fav_element__categories__cat=categorie).delete()

        user_id = User.objects.get(id=request.user.id)

        for i in favorites:
            print(i)
            elem = Element.objects.get(categories__cat = categorie, element__kat_element=i)

            fav = FavoriteElement(
                user_id = user_id,
                fav_element = elem
            )

            fav.save()


    return render(request, 'options.html',
                  {'massage': messages}
                  )

def addcalc(request):

    addform = CalcForm()
    delform = calcchoiceform()

    if request.method == 'POST':

        calc = CalcForm(request.POST)
        enf = calcchoiceform(request.POST)

        if calc.is_valid():
            calc = calc.cleaned_data['calc']
            q = Calc_Choices(
                 calc=calc
            )

            q.save()

            messages.success(request, ' Erfolgreich Gespeichert')

        if enf.is_valid():
            enf = enf.cleaned_data['choice']

            q = Calc_Choices.objects.get(calc=enf)
            q.delete()

            messages.success(request, 'Eintrag gelöscht')

    return render(request, 'addcalc.html',
                  {'addform': addform,
                   'delform': delform}
                  )


def ajax_table(request):

    typ = Categorie.objects.all()
    kat_element = ElementTOKat.objects.all().order_by('katgroup__kategorie')
    load_table = Element.objects.all()
    calc_choices = Calc_Choices.objects.all()

    return render(request, 'ajax_table.html',
                  {
                      'load_table': load_table,
                      'typ': typ,
                      'kat_element': kat_element,
                      'calc_choices': calc_choices
                  })

def admin_options(request):

    typ = Categorie.objects.all()
    kat = Kategorie.objects.all().order_by('kategorie')
    kat_element = ElementTOKat.objects.all().order_by('katgroup__kategorie')
    load_table = Element.objects.all()
    elements = ElementTOKat.objects.all().values_list('ele__kat_element', flat=True)
    userform =  MyRegistrationForm()
    user = request.user

    if request.method == 'POST':
        user = MyRegistrationForm(request.POST)
        print(user)
        print('valid_test')

        print("valid")
        email = user.cleaned_data['email']
        username = user.cleaned_data['username']
        first_name = user.cleaned_data['first_name']
        last_name = user.cleaned_data['last_name']
        is_superuser = user.cleaned_data['is_superuser']

        print(email)
        print(username)
        print(first_name)
        print(last_name)
        print(is_superuser)

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            is_superuser=is_superuser
        )

        print(user)
        user.save()

        messages.success(request, 'Account created successfully')

    return render(request, 'admin_options.html',
                  {
                      'kat': kat,
                      'load_table': load_table,
                      'typ': typ,
                      'kat_element': kat_element,
                      'userform': userform,
                      'user': user
                  })

def load_favelements(request):

    if request.method == 'POST':
        cat = request.POST['categorie']

        fav_kat_element = ElementTOKat.objects.filter(katgroup__kategorie=cat).values_list('ele', flat=True)
        kat_element = KategorieElement.objects.exclude(id__in=fav_kat_element)

    return render(request, 'load_elements_opt.html',
                  {
                   'kat_element': kat_element,
                   'fav_kat_element': fav_kat_element}
                  )

def load_fav(request):

    if request.method == 'POST':
        cat = request.POST['categorie']

        fav_kat_element = Element.objects.filter(categorie=cat).order_by('element').values_list('element', flat=True)


    return render(request, 'load_favelements.html',
                  {
                   'fav_kat_element': fav_kat_element}
                  )


def load_combination(request):

    if request.method == 'POST':
        data = request.POST

        Element.objects.all().delete()

        import time

        start_time =time.time()

        for key in data.keys():
            if key == 'csrfmiddlewaretoken':
                continue
            row = data.getlist(key,'')
            print(row)

            if row[5]=='true':
                q = Element(
                    element = KategorieElement.objects.get(kat_element=row[0]),
                    wie = row[1],
                    obj = row[2],
                    kategorie= Kategorie.objects.get(kategorie=row[3]),
                    categories= Categorie.objects.get(cat=row[4]),
                    calc = Calc_Choices.objects.get(calc=row[6])
                )

                q.save()
        print('save time: ' + str(time.time() - start_time))
    return render(request, 'admin_options.html',
                  {}
                  )


def load_categorie(request):

    if request.method == 'POST':
        try:
            favorites = request.POST['favorites']
            favorites = favorites.split(",")[1:]
        except:
            favorites = None

        categorie = request.POST['categorie']

        cat = Kategorie.objects.get(kategorie=categorie)

        from django.core.exceptions import ObjectDoesNotExist
        try:
           ElementTOKat.objects.filter(katgroup=cat).delete()

        except (ObjectDoesNotExist):
            pass
        if favorites is not None:
            for f in favorites:
                fav = KategorieElement.objects.get(kat_element=f)

                q = ElementTOKat(
                    katgroup= cat,
                    ele=fav
                )

                q.save()

    return render(request, 'admin_options.html',
                  {}
                  )

