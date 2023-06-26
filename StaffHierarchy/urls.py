from django.contrib import admin
from django.urls import path, include
from tree_structure.views import tree_structure, database
from account.views import registration_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tree_structure, name='tree_structure'),
    path('database/', database, name='database'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('manager/', include('manager.urls')),
]
