from django.shortcuts import render, redirect
from .models import Metric
from .import forms


def minput(request):
    if request.method == 'POST':
        form = forms.Metric(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = request.user
            record.save()
            return redirect('metric:metric')

    else:
        form = forms.Metric()
        return render(request, 'minput.html', {'form': form})


def moutput(request):
    metricdisplay = Metric.objects.all()
    return render(request, 'moutput.html', {'metric': metricdisplay})


def bmimetric(request):

    return render(request, 'bmimetric.html')
