from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import TopManager, Director, RegionalManager, DistrictManager, Teamlead, Specialist, Trainee

@admin.register(TopManager)
class TopManagerAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(RegionalManager)
class RegionalManagerAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(DistrictManager)
class DistrictManagerAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(Teamlead)
class TeamleadAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }

@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ["position", "surname", "name", ]
    list_filter = ('head', )
    prepopulated_fields = {'slug': ('position', 'surname', 'name'), }