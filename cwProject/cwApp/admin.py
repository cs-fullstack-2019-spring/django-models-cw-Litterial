from django.contrib import admin

# Register your models here.
from .models import Dog
from .models import newAccount

admin.site.register(Dog)
admin.site.register(newAccount)