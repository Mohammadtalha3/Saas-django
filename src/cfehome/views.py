from django.http import HttpResponse
from django.shortcuts import render
from visits.models import  Page_Vists






def home_page_view(request, *args, **kwargs):
    Page_Vists.objects.create(path= request.path)

    queryset= Page_Vists.objects.filter(path= request.path)

    my_title= 'muhammad talha'

    context= {
        "page_title": my_title,
        "page_visit_count": queryset.count()
    }
    #page_vists.objects.create()

    return render(request, template_name='home.html', context=context)