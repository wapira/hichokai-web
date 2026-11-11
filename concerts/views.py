from django.shortcuts import render, get_object_or_404
from .models import Concert, ConcertRecord

# Create your views here.
def concert_list(request):
    concerts = Concert.objects.order_by("-year", "-date")
    
    return render(request, "concerts/concert_list.html", {"concerts": concerts})


def concert_detail(request, pk):
    concert = get_object_or_404(Concert, pk=pk)
    records = ConcertRecord.objects.filter(concert=concert).order_by("number") 
    return render(request, "concerts/concert_detail.html", {"concert": concert, "records": records})