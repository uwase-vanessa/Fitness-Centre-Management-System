from django.contrib import admin
from.models import Customer
from django.contrib.auth.models import Group

admin.site.site_header= 'BeFiter Dashboard'

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','category','hours',)
    list-filter=('category'                                                                                                                                                                                                                                                                                                                                                                                                     )

# Register your models here
admin.site.register(Customer)
#admin.site.unregister(Group)


