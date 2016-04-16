from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
# Create your models here.

CATEGORY = (  
	('GN', 'General'),
	('OBC', 'OBC'),
	('SC/ST', 'SC/ST'),
)
LOCATIONS = (
    ('Maharastra', 'Maharastra'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Delhi', 'Delhi'),
    ('West Bangal', 'West Bangal'),
)


class Userprofile(models.Model):  
    user = models.OneToOneField(User)  
    category = models.CharField(max_length=20, choices=CATEGORY)
    state = models.CharField(max_length=20, choices=LOCATIONS)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):  
          return "%s's profile" % self.user



def create_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, new = Userprofile.objects.get_or_create(user=instance)  

post_save.connect(create_profile, sender=User) 


@python_2_unicode_compatible
class options(models.Model):
	option_name = models.CharField(max_length=200, default='Scholarship')
	option_state = models.CharField(max_length=20, choices=LOCATIONS, default='MH')
	option_category = models.CharField(max_length=20, choices=CATEGORY, default='GN')
	option_amount = models.IntegerField(default=0)

	def __str__(self):
		return self.option_name