from diary.views.note import note_and_next_hx, create_note_hxpost
from diary.views.start import start_page
from django.urls import path

urlpatterns = [
    path('', start_page, name='start_page'),
    path('create_note_hxpost', create_note_hxpost, name='create_note_hxpost'),
    path('note_and_next_hx/<note_id>', note_and_next_hx, name='note_and_next_hx'),
]