from django.contrib import admin
#we must import the table name
from firstapp.models import Contact,Signupdata


#register the models here
admin.site.register(Contact)
admin.site.register(Signupdata)
#after completing this then make migrations

