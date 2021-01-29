from diary.models import Note
from django.forms import Textarea, ModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.html import format_html
from django.views.generic import ListView, CreateView


class NoteListView(ListView):
    model = Note

    @classmethod
    def hx_create_view(cls):
        return format_html('<div hx-get="{}" hx-trigger="load" hx-swap="outerHTML"></div>', reverse('note-create'))

    @classmethod
    def hx_first_read_view(cls):
        first = Note.objects.all().order_by('-datetime', '-id').first()
        if not first:
            return ''
        return note_and_next_html(first)

class NoteCreateForm(ModelForm):
    class Meta:
        fields = ['datetime', 'title', 'text']
        model = Note
        widgets = {
            'text': Textarea(attrs={'rows': 3}),
        }

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm

    def form_valid(self, form):
        # No Post/Redirect/Get needed for htmx
        instance = form.save()
        return HttpResponse(
            format_html('{} {}', NoteListView.hx_create_view(), note_html(instance)))


def get_next_or_none(note):
    # SQLite does not store mircoseconds. Two entries added in one second can't be
    # distinguished with ".first()". Grrr ugly loop is needed.
    found = False
    for next in Note.objects.filter(datetime__lte=note.datetime).order_by('-datetime', '-id'):
        if found:
            return next
        if next==note:
            found = True

def note_html(note):
    return format_html('''
    <h1>{date} {title}</h1>
    <p>{text}</p>
    ''', date=note.datetime.strftime('%d.%b'), title=note.title, text=note.text)

def note_and_next(request, pk):
    return HttpResponse(note_and_next_html(get_object_or_404(Note, pk=pk)))

def note_and_next_html(note):
    next = get_next_or_none(note)
    if next:
        hx_next = format_html('<div hx-get="{}" hx-trigger="revealed" hx-swap="outerHTML">...</div>',
                              reverse('note_and_next', kwargs=dict(pk=next.id)))
    else:
        hx_next = 'The End'
    return format_html('{note_html} {hx_next}',
                                    note_html=note_html(note),
        hx_next=hx_next)
