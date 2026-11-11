from django.db import models
from scores.models import Score

class Concert(models.Model):
    name = models.CharField("演奏会名", max_length=50, unique=True)
    date = models.DateField("日付", null=True, blank=True)
    year = models.PositiveIntegerField("年")
    place = models.CharField("場所", max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.name}/{self.year}"
        
    class Meta:
        verbose_name = "演奏会"
        verbose_name_plural = "演奏会"
    
    
class ConcertRecord(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, verbose_name="演奏会")
    score = models.ForeignKey(Score, on_delete=models.PROTECT, verbose_name="楽譜")
    number = models.PositiveIntegerField("曲順")
    youtube_url = models.URLField("Youtube動画URL", blank=True)
    note = models.CharField("備考", max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.concert}/{self.score}"
        
    class Meta:
        verbose_name = "演奏記録"
        verbose_name_plural = "演奏記録"
        ordering = ["number"]
    
