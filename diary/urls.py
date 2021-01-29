from diary.views import NoteListView, NoteCreateView, note_and_next
from django.urls import path

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('note/create', NoteCreateView.as_view(), name='note-create'),
    path('note/<pk>/and_next', note_and_next, name='note_and_next'),

]