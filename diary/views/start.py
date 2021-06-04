from diary.models import Note
from diary.views.common import page
from diary.views.note import note_add_html, note_and_next_html
from django.utils.html import format_html


def start_page(request):
    return page(format_html('''
     {note_add}
     {first_note}''', note_add=note_add_html(), first_note=first_note()))


def first_note():
    first = Note.objects.all().order_by('-datetime', '-id').first()
    if not first:
        return ''
    return note_and_next_html(first)
