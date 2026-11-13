from django.shortcuts import render
from concerts.models import Concert
from django.utils import timezone

# Create your views here.
def home(request):
    
    next_concert = Concert.objects.filter(date__gte=timezone.localdate()).order_by("date").first()
    return render(request, "pages/home.html", {"next_concert": next_concert})
