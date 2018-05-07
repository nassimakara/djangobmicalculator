from django.shortcuts import render

# Welcome Page of the Application


def welcome(request):

    return render(request, 'bmiapp.html')

# About Us page of the application


def aboutus(request):

    return render(request, 'aboutus.html')


# Page explaining what the definition of the BMI calculator


def bmi(request):

    return render(request, 'bmi.html')
