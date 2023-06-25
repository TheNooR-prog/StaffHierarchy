from django.contrib import admin
from django.urls import path
from tree_structure.views import tree_structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tree_structure),

]
