from django.contrib import admin
from . models import Msgs
# Register your models here.
admin.site.register(Msgs)

class Table(admin.ModelAdmin):
	class meta:
		model = Msgs

