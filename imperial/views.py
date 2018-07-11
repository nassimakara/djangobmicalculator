from django.shortcuts import render, redirect
from .models import Imperial
from .import forms


def impinput(request):
    if request.method == 'POST':
        form = forms.Impcalc(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = request.user
            record.save()
            return redirect('imperial:impoutput')

    else:
        form = forms.Impcalc()
        return render(request, 'impinput.html', {'form': form})


def impoutput(request):
    imperialdisplay = Imperial.objects.all()
    return render(request, 'impoutput.html', {'imperial': imperialdisplay})


def bmiimperial(request):

    return render(request, 'bmiimperial.html')
