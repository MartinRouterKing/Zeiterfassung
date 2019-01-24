from tracking.models import Element, Categorie, Workingtime, FavoriteElement, ElementTOKat
from tracking.models import KategorieElement, Kategorie, Calc_Choices
from .forms import Choicefrom, Categorieform, editcatForm, Worktimefrom, deletecatForm, CalcForm,\
    Elementform, editelechoiceform, SignupForm, Categoriechoiceform, calcchoiceForm, editCalcForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, UsereditForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

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

    return render(request, 'options/load_favorites.html',
                  {'favorites': favorites}
                  )

def options(request):
    choice_form = Choicefrom(request.POST)
    return render(request,'options/options.html',
                  {
                      'choice_form': choice_form,

                   })

def addcategories(request):

    '''
    Add a new categorie the the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: categorie (TextField)
    :return: save the Text input to the Database
    '''

    if request.method == 'POST':
        categorieform = Categorieform(request.POST)
        print(request.POST)
        print(categorieform)
        if categorieform.is_valid():
            cat = categorieform.cleaned_data['cat']
            try:
                Categorie.objects.get(cat=cat)
            except ObjectDoesNotExist:
                ca = Categorie(
                    cat = cat
                )
                ca.save()
                messages.success(request, ' Erfolgreich gespeichert')
            else:
                messages.warning(request, "Warnung: " + cat + " ist bereits vorhanden. Der Eintrag wurde nicht gespeichert." )
        else:
            messages.warning(request, 'Warnung: Bitte Überprüfen Sie die Eingabe')

    return render(request, 'options/addcategories.html',
                  {'categorieform': Categorieform}
                  )

def editcategories(request):
    '''
    Edit the categories in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice and editform
    :return: Uppdate the selected choice in the model
    '''

    editcatform = editcatForm()


    if request.method == 'POST':
        form = editcatForm(request.POST)


        if form.is_valid():
            choice = form.cleaned_data['choice']
            edit = form.cleaned_data['edit']
            q = Categorie.objects.get(cat=choice)
            q.cat= edit
            q.save()
            messages.success(request, ' Erfolgreich gespeichert')
        else:
            messages.warning(request, 'Warnung: Bitte Überprüfen Sie die Eingabe')

    return render(request, 'options/editcategories.html',
                  {'editcatform': editcatform}
                  )

def deletecategories(request):

    '''
    Delete elements in the Datamodel
    ClickEvent popup a new window with the input mask

    :param request: choice
    :return: Delete the selected categorie
    '''

    choice = deletecatForm()

    if request.method == 'POST':
        choice = deletecatForm(request.POST)
        if choice.is_valid():
            edit = choice.cleaned_data['choice']
            Categorie.objects.filter(cat=edit).delete()
            messages.success(request, 'Erfolgreich Gelöscht')

    return render(request, 'options/deletecategories.html',
                  {'choice': choice}
                  )


def addelements(request):
    if request.method == 'POST':
        elementsform = Elementform(request.POST)
        if elementsform.is_valid():
            elements = elementsform.cleaned_data['kat_element']
            try:
                KategorieElement.objects.get(kat_element=elements)
            except ObjectDoesNotExist:

                ca = KategorieElement(
                    kat_element = elements
                )

                ca.save()

                messages.success(request, ' Erfolgreich gespeichert')

            else:
                messages.warning(request, "Warnung: " + elements + " ist bereits vorhanden")


    return render(request, 'options/addelements.html',
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

            q.kat_element = txt
            q.save()
            messages.success(request, ' Erfolgreich gespeichert')
        else:
            messages.warning(request, ' Bitte Überprüfen Sie die Eingabe')

    return render(request, 'options/editelements.html',
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

    return render(request, 'options/deleteelements.html',
                  {'choice': choice}
                  )
def addfavortites(request):

    if request.method == 'POST':

        categorie = request.POST['categorie']

        favorites = request.POST.get('favorites', False)


        if favorites==False:
            FavoriteElement.objects.filter(fav_element__categories__cat=categorie).delete()
        else:
            favorites = favorites.split(",")[1:]

            FavoriteElement.objects.filter(fav_element__categories__cat=categorie).delete()

            user_id = User.objects.get(id=request.user.id)

            for i in favorites:

                elem = Element.objects.get(categories__cat = categorie, element__kat_element=i)

                fav = FavoriteElement(
                    user_id = user_id,
                    fav_element = elem
                )

                fav.save()


    return render(request, 'options/options.html',
                  {'massage': messages}
                  )

def addcalc(request):
    addform = CalcForm()
    if request.method == 'POST':
        calc = CalcForm(request.POST)
        if calc.is_valid():
            calc = calc.cleaned_data['calc']
            try:
                check = Calc_Choices.objects.get(calc=calc)

            except ObjectDoesNotExist:

                q = Calc_Choices(
                     calc=calc
                )

                q.save()

                messages.success(request, 'Erfolgreich Gespeichert')
            else:
                messages.warning(request, "Warnung: " + calc + " ist bereits vorhanden")

    return render(request, 'options/addcalc.html',
                  {'addform': addform}
                  )

def editcalc(request):
    editcalcform = editCalcForm()
    if request.method == 'POST':
        editcalcform = editCalcForm(request.POST)
        if editcalcform.is_valid():
            choice = editcalcform.cleaned_data['choice']
            edit = editcalcform.cleaned_data['edit']

            q = Calc_Choices.objects.get(calc=choice)
            q.calc = edit

            q.save()
            messages.success(request,'Kostenträger erfolgreich geändert')

        else:
            messages.error(request, "Fehler! Bitte überprüfen Sie die Eingabe")

    return render(request, 'options/editcalc.html',
                  {'editcalcform': editcalcform}
                  )


def deletecalc(request):
    delform = calcchoiceForm()
    if request.method == 'POST':
        enf = calcchoiceForm(request.POST)
        if enf.is_valid():
            enf = enf.cleaned_data['choice']
            q = Calc_Choices.objects.get(calc=enf)
            q.delete()
            messages.success(request, 'Eintrag gelöscht')
        else:
            messages.error(request, "Fehler! Bitte überprüfen Sie Ihre Eingaben.")
    return render(request, 'options/deletecalc.html',
                  {'delform': delform}
                  )


def admin_options(request):
    cat_choice = Categoriechoiceform()
    typ = Categorie.objects.all().order_by('cat')
    kat = Kategorie.objects.all().order_by('kategorie')
    calc = Calc_Choices.objects.all()
    kat_element = ElementTOKat.objects.all().order_by('katgroup__kategorie')
    load_table = Element.objects.filter(categories=13)
    elements = KategorieElement.objects.all().order_by('kat_element')
    userform = SignupForm()
    user = request.user

    if request.method == 'POST':
        signupform = SignupForm(request.POST)

        if signupform.is_valid():
            to_email = signupform.cleaned_data.get('email')
            try:
                match = User.objects.get(email=to_email)

            except ObjectDoesNotExist:
                user = signupform.save(commit=False)
                user.is_active = True
                user.save()

                from mail_templated import EmailMessage

                current_site = get_current_site(request)

                message = EmailMessage('email\login.tpl', {'user': user,
                                                           'domain': current_site.domain,
                                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                                                           'token': PasswordResetTokenGenerator().make_token(user)}, to=[user.email])

                message.send()


                messages.success(request, 'Benutzer wurde erfolgreich erstellt und eine E-Mail Verrifizierung an ' + to_email + ' versendet.')

            else:
                messages.warning(request,'E-Mail ' + to_email + ' ist bereits vergeben.')

        else:
            messages.warning(request, 'Warnung: Benutzername oder E-mail bereits vergeben.')

    return render(request, 'options/admin_options.html',
                  {
                      'kat': kat,
                      'elements': elements,
                      'calc': calc,
                      'cat_choice': cat_choice,
                      'load_table': load_table,
                      'typ': typ,
                      'kat_element': kat_element,
                      'userform': userform,
                      'user': user
                  })

def load_favelements(request):

    # EVTL RAUS?!

    if request.method == 'POST':
        cat = request.POST['categorie']
        # WARUM ELEMENTTOKAT?
        fav_kat_element = ElementTOKat.objects.filter(katgroup__kategorie=cat).values_list('ele', flat=True)
        kat_element = KategorieElement.objects.exclude(id__in=fav_kat_element)

    return render(request, 'options/load_elements_opt.html',
                  {
                   'kat_element': kat_element,
                   'fav_kat_element': fav_kat_element}
                  )

def load_fav(request):

    if request.method == 'POST':
        cat = request.POST['categorie']

        fav_kat_element = Element.objects.filter(categories__cat=cat).order_by('element').values_list('element', flat=True)

    return render(request, 'options/load_favelements.html',
                  {
                   'fav_kat_element': fav_kat_element}
                  )

def ajax_save_element(request):
    if request.method == "POST":

        element = request.POST.getlist('element[]')
        cat_choice = request.POST['cat_choice']
        wie = request.POST.getlist('wie[]')
        obj = request.POST.getlist('obj[]')
        calc = request.POST.getlist('calc[]')


        try:
            d = Element.objects.filter(categories__cat = cat_choice)
            d.delete()
        except ObjectDoesNotExist:
            print('PROBLEM')

        for i in range(len(element)):

            q = Element(
                categories =  Categorie.objects.get(cat=cat_choice),
                element = KategorieElement.objects.get(kat_element=element[i]),
                wie = wie[i],
                obj = obj[i],
                calc = Calc_Choices.objects.get(calc=calc[i])
            )

            q.save()

    return render(request, 'options/admin_options.html' ,
           {}
           )


def ajax_add_from_group(request):

    counter = request.POST['counter']
    elements = KategorieElement.objects.all()
    calc = Calc_Choices.objects.all()

    return render(request, 'options/add_form_group.html' ,
                  {'counter': counter,
                   'elements': elements,
                   'calc': calc}
                  )

def ajax_load_from_groups(request):

    cat_choice = request.POST['cat_choice']

    elements = KategorieElement.objects.all().order_by('kat_element')
    load_table = Element.objects.filter(categories__cat=cat_choice)
    calc = Calc_Choices.objects.all()

    return render(request, 'options/ajax_load_from_groups.html',
                  {
                      'elements':elements,
                      'load_table': load_table,
                      'calc': calc
                   }
                  )

def edit_user(request):
    usereditform = UsereditForm()

    if request.method == 'POST':
        usereditform = UsereditForm(request.POST)
        if usereditform.is_valid():
            username = usereditform.cleaned_data['username']
            email = usereditform.cleaned_data['email']
            first_name = usereditform.cleaned_data['first_name']
            last_name = usereditform.cleaned_data['last_name']
            working_time = usereditform.cleaned_data['working_time']

            try:
                match = User.objects.get(email=email)

                if str(match.username) == str(username):
                    messages.success(request, "Benutzerdaten wurden gespeichert")
                    match.email = email
                    match.first_name = first_name
                    match.last_name = last_name
                    match.save()

                    time = Workingtime(
                        workingtime= working_time,
                        user_id = User.objects.get(username=username)
                    )
                    time.save()
                else:
                    messages.warning(request,"E-Mail Adresse ist bereits vergeben")

            except ObjectDoesNotExist:
                messages.success(request, "Benutzerdaten wurden gespeichert")
                # Unable to find a user, this is fine
                q = User.objects.get(username=username)
                q.email = email
                q.first_name = first_name
                q.last_name = last_name
                q.save()
        else:
            messages.warning(request,"Hoppla, da ist wohl etwas schief gelaufen. Bitte laden Sie die Seite erneut!")
    return render(request, 'options/edit_user.html',
                  {
                      'usereditform': usereditform}
                  )

def ajax_load_userdata(request):

    if request.method == 'POST':
        usereditform = UsereditForm()
        selecteduser = request.POST['selecteduser']
        options = User.objects.all()
        userdata = User.objects.get(id=selecteduser)
        try:
            workingtime = Workingtime.objects.get(user_id=selecteduser)
            workingtime = workingtime.workingtime

        except ObjectDoesNotExist:
            workingtime = ""

    return render(request, 'options/ajax_load_userdata.html',

                  {   'options': options,
                      'workingtime': workingtime,
                      'userdata': userdata}
                  )