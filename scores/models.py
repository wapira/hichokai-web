from django.db import models

# Create your models here.
class Instrument(models.Model):
    name = models.CharField("楽器名", max_length=15, unique=True)
      
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "楽器"
        verbose_name_plural = "楽器"
    
class Score(models.Model):
    name = models.CharField("曲名", max_length=50, unique=True)
    name_kana = models.CharField("ふりがな", max_length=50)
    composer = models.CharField("作曲者", max_length=50)
    note = models.TextField("備考", blank=True)
    instrumentation = models.ManyToManyField(Instrument, through="ScorePart", verbose_name="編成")
    
    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = "楽譜"
            verbose_name_plural = "楽譜"
            
class ScorePart(models.Model):
    score = models.ForeignKey(Score, on_delete=models.CASCADE, verbose_name="楽譜")
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT, verbose_name="楽器")
    count = models.PositiveIntegerField("パート数")
    
    def __str__(self):
        return f"{self.instrument}{self.count}"
    
    class Meta:
        verbose_name = "楽譜編成"
        verbose_name_plural = "楽譜編成"
        constraints = [
            models.UniqueConstraint(fields=["score", "instrument"],name="scores_scorepart_unique_score_instrument"),
        ]
    