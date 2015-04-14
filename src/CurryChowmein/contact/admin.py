from django.contrib import admin
from .models import ContactUs

# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
	class Meta:
		model = ContactUs

		
admin.site.register(ContactUs,ContactUsAdmin)
