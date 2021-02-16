from django.shortcuts import render, redirect


def dashboard(request):
    template_name = 'admins/dashboard.html'

    context = {}

    return render(request, template_name, context)
