from django.contrib import admin
from django.urls import path
from app.views import lpu, aboutlpu, home, saveDataView, deleteView

urlpatterns = [
    path('', home, name='home'),
    path('lpu/', lpu, name='lpu'),
    path('aboutlpu/', aboutlpu, name='aboutlpu'),
    path('save_data/', saveDataView, name='save_data'),
    path('delete-note/<int:id>/', deleteView, name="deleteView"),
]
