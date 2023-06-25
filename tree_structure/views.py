from django.shortcuts import render, HttpResponse
from .models import TopManager, Director, RegionalManager, DistrictManager, Teamlead, Specialist, Trainee

# Create your views here.
def tree_structure(request):
    top_managers = TopManager.objects.all()
    directors = Director.objects.all()
    regional_managers = RegionalManager.objects.all()
    district_managers = DistrictManager.objects.all()
    teamleads = Teamlead.objects.all()
    specialists = Specialist.objects.all()
    trainees = Trainee.objects.all()

    data = {'top_managers': top_managers,
            'directors': directors,
            'regional_managers': regional_managers,
            'district_managers': district_managers,
            'teamleads': teamleads,
            'specialists': specialists,
            'trainees': trainees,
            }

    return render(request, 'tree_structure.html', context=data)