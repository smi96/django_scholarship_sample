from django.contrib import admin
from .models import Userprofile
from .models import options

# Register your models here.
admin.site.register(Userprofile, )
admin.site.register(options)