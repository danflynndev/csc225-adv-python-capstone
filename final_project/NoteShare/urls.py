from django.urls import path
from . import views

app_name = 'NoteShare'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create_note, name='create_note'),
    path('edit/<note_id>', views.edit_note, name='edit_note'),
    path('share/<note_id>', views.share_note, name='share_note'),
    path('delete/<note_id>', views.delete_note, name='delete_note'),
    path('hide/<note_id>', views.hide_note, name='hide_note')
]