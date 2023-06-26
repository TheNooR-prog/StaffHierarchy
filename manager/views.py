from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from tree_structure.models import TopManager, Director, RegionalManager, DistrictManager, Teamlead, Specialist, Trainee

# Create your views here.
def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def hierarchy_manage(request):

    return render(request, 'hierarchy_manage.html')

