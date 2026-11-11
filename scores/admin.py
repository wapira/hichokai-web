from django.contrib import admin
from .models import Instrument, Score, ScorePart

class ScorePartInline(admin.TabularInline):
    model = ScorePart
    extra = 2
    
class ScoreAdmin(admin.ModelAdmin):
    inlines = [ScorePartInline]
    search_fields = ["name", "name_kana", "composer"]

admin.site.register(Instrument)
admin.site.register(Score, ScoreAdmin)

