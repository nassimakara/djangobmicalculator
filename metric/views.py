from django.shortcuts import render, redirect
from .models import Metric
from .import forms


def minput(request):
    if request.method == 'POST':
        form = forms.Mcalc(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = request.user
            record.save()
            return redirect('metric:moutput')

    else:
        form = forms.Mcalc()
        return render(request, 'metric/minput.html', {'form': form})


def moutput(request):
    metricdisplay = Metric.objects.all().order_by('patient')
    return render(request, 'metric/moutput.html', {'metric': metricdisplay})

def bmimetric(request):
    return render(request, 'metric/bmimetric.html')


