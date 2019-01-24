{% extends "mail_templated/base.tpl" %}

{% block subject %}
 Arbeitszeiterfassung: Erinnerung
{% endblock %}

{% block body %}
{{ u.name }}, this is a plain text message.
{% endblock %}

{% block html %}
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">


<div style="height: 100px; background-color: #24282c;">
    <center>
        <i style="color: white; font-size: 30px; padding-top: 40px;" class="fas fa-user-clock"></i>
        <div style="color: white;">Arbeitszeiterfassung</div>
    </center>
</div>
        <div style="background-color: #f2f2f2; padding: 10px;">
        <p class="text-primary" style="font-size: 18px; background-color: #f2f2f2; padding-top: 10px;">Guten Tag {{ u.username }},</p>
        <p class="text-justify" style="background-color: #f2f2f2;">sicher hast du bereits deine Arbeitszeit für diesen Monat dokumentiert.</p>
        <p class="text-justify" style="background-color: #f2f2f2;">Vorsichtshalber möchte ich dich noch einmal daran erinnern, dass dir nur noch wenige Tage bleiben, bis der Zugriff für dieser Monat erlischt.</p>
        <p class="text-justify" style="background-color: #f2f2f2;">Logge dich doch schnell ein, um deine bisherigen Stunden zu überprüfen oder weitere einzutragen.</p>

        <a href="{{link}}">Zum Login</a>

        </div>
    <div style=" height: 50px; position: relative; background-color: #24282c;">
    </div>
{% endblock %}
