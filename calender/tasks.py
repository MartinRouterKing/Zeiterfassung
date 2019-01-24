from background_task import background
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
import pytz
from django.contrib.sites.shortcuts import get_current_site

@background(schedule=5)
def notify_user():
    print("TASK")
    # lookup user by id and send them a message
    user = User.objects.all()
    today = pytz.utc.localize(datetime.datetime.utcnow())
    for u in user:

        last_login = u.last_login

        if last_login is None:
            continue
        else:
            offline = today - u.last_login
            if offline > timedelta(days=5):

                from_email = 'wiefoetimetracking@gmail.com'
                link = "http://127.0.0.1:8000/"
                from mail_templated import EmailMessage

                message = EmailMessage('email\\reminder.tpl', {'u': u, 'link': link}, to=[u.email])
                # TODO: Add more useful commands here.
                message.send()

