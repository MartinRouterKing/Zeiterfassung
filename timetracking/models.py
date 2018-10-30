from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # If titulo is empty set it to the username.
        # Now call the save() method on super to store the instance.
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name()
        #return self.personal_first_name + ' - ' + self.personal_last_name





