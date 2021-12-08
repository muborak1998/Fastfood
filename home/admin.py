from django.contrib import admin
from home.models import ContactMessage, Aboutus, Chef


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'creat_at',)
    list_filter = ['status']


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone', 'country', 'city', 'image', 'description']

class ChefAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Chef, ChefAdmin)