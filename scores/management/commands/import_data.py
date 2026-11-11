import csv
from scores.models import Instrument, Score, ScorePart
from concerts.models import Concert, ConcertRecord
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):
    help = "演奏データをCSVで取り込む"

    def handle(self, *args, **options):
        self.import_scores()
        self.import_concerts()
        self.import_records()
        
    def import_scores(self):
        with open("data/scores.csv", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        score, created = Score.objects.get_or_create(name=row["曲名"], 
                                                                     defaults={
                                                                     "name_kana":row["ふりがな"], 
                                                                     "composer":row["作曲者"], 
                                                                     "note":row["備考"]
                                                                     },)
                        parts = row["編成"].split(";")
                        for part in parts:
                            name = part[:-1]
                            count = int(part[-1])
                            instrument = Instrument.objects.get(name=name)
                            score_part, created = ScorePart.objects.get_or_create(score=score, 
                                                                                  instrument=instrument,
                                                                                  defaults={ 
                                                                                  "count":count},)   
    
    def import_concerts(self):
        with open("data/concerts.csv", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["日付"]:
                    concert_date = datetime.strptime(row["日付"], "%Y/%m/%d").date()
                else:
                    concert_date = None
                concert, created = Concert.objects.get_or_create(name=row["演奏会名"],
                                                                 defaults={
                                                                     "date":concert_date,
                                                                     "year":int(row["年"]),
                                                                     "place":row["場所"]
                                                                 })
    
    def import_records(self):
        with open("data/records.csv", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                concert = Concert.objects.get(name=row["演奏会名"])
                score = Score.objects.get(name=row["曲名"])
                record, created = ConcertRecord.objects.get_or_create(concert=concert, 
                                                                      score=score,
                                                                      defaults={
                                                                          "number":int(row["曲順"]), 
                                                                          "youtube_url":row["Youtube動画URL"],
                                                                          "note":row["備考"]
                                                                                 },)
                                    