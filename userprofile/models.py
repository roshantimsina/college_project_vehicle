from __future__ import unicode_literals

import hashlib
import os.path
import urllib

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from activities.models import Notification

GENDER_CHOICES = (
        ('Male' , 'Male'),
        ('Female' , 'Female'),
    )


python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length= 10, choices= GENDER_CHOICES, default=0, null=True, blank= True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    


    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
    	return "user:{}".format(self.user)

    def get_picture(self):
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' +\
                self.user.username + '_tmp.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' +\
                self.user.username + '_tmp.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = 'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d': no_picture, 's': '256'})
                    )
                return gravatar_url

        except Exception:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username



    def notify_booked(self, vehicle):
        if self.user != vehicle.user:
            Notification(notification_type=Notification.BOOKED,
                         from_user=self.user, to_user=vehicle.user,
                         vehicle=vehicle).save()

    def unotify_booked(self, vehicle):
        if self.user != vehicle.user:
            Notification.objects.filter(
                notification_type=Notification.BOOKED,
                from_user=self.user,
                to_user=vehicle.user,
                vehicle=vehicle).delete()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
