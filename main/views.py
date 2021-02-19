from django.shortcuts import render

from .forms import FilterForm

def homepage(request):

    form = FilterForm()


    template_name = 'main/index.html'

    context = {
        'form':form,
    }
    
    return render(request, template_name, context)