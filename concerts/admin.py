from django.contrib import admin
from .models import Concert, ConcertRecord

class ConcertRecordInline(admin.TabularInline):
    model = ConcertRecord
    extra = 2
    autocomplete_fields = ["score"]
    
class ConcertAdmin(admin.ModelAdmin):
    inlines = [ConcertRecordInline]
    
admin.site.register(Concert, ConcertAdmin)