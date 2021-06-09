from django.contrib import admin
from .models import team
from django.utils.html import format_html
# Register your models here.
class teamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.image.url))
    
    thumbnail.short_desricription = 'image'
    list_display=('id','thumbnail','first_name','designation','created_date')
    list_display_links = ('first_name','id','thumbnail')
    search_fields =('first_name','last_name','designation')
    list_filter = ('designation',)
admin.site.register(team,teamAdmin)