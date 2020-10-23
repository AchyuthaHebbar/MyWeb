from django.shortcuts import render
from .forms import JatakaForm
from .astro import Astro


# Create your views here.
def jataka_home(request):
    if request.method == 'POST':
        form = JatakaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            place = form.cleaned_data['birth_place']
            dob = str(form.cleaned_data['date_of_birth'])
            tob = str(form.cleaned_data['time_of_birth'])
            lat = str(form.cleaned_data['latitude'])
            lon = str(form.cleaned_data['longitude'])
            kund = Astro(place,dob,tob,lat,lon,name)
            return render(request, 'jataka/horoscope.html', {'kund':kund})
    else:
        form = JatakaForm()
    return render(request, "jataka/jataka_home.html", {'form':form})
