from django.urls import path
from .views import hierarchy_manage

app_name = 'manager'

urlpatterns = [
    path('hierarchy_manage/', hierarchy_manage, name='hierarchy_manage'),
]