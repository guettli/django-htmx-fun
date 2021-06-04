from diary.models import Note
from django.forms import ModelForm, Textarea
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.html import format_html

from django.views.decorators.http import require_POST


class NoteCreateForm(ModelForm):
    class Meta:
        fields = ['datetime', 'title', 'text']
        model = Note
        widgets = {
            'text': Textarea(attrs={'rows': 3}),
        }


def note_add_html():
    form = NoteCreateForm()
    return note_form_html(form)


def note_form_html(form):
    return format_html(
        '''
    <form hx-post="{url}">
     {form}
     <input type="submit">
    </form>''',
        url=reverse(create_note_hxpost),
        form=form,
    )


def note_html(note):
    return format_html(
        '''
    <h1>{date} {title}</h1>
    <p>{text}</p>
    ''',
        date=note.datetime.strftime('%d.%b'),
        title=note.title,
        text=note.text,
    )


def note_hx(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return HttpResponse(note_html(note))


@require_POST
def create_note_hxpost(request):
    form = NoteCreateForm(request.POST)
    if form.is_valid():
        note = form.save()
        return HttpResponse(format_html('{} {}', note_add_html(), note_html(note)))
    return HttpResponse(note_form_html(form))


def note_and_next_html(note):
    next = get_next_or_none(note)
    if next:
        next_html = format_html(
            '<div hx-get="{}" hx-trigger="revealed" hx-swap="outerHTML">...</div>',
            reverse('note_and_next_hx', kwargs=dict(note_id=next.id)),
        )
    else:
        next_html = 'The End'
    return format_html(
        '{note_html} {next_html}', note_html=note_html(note), next_html=next_html
    )


def get_next_or_none(note):
    # SQLite does not store mircoseconds. Two entries added in one second can't be
    # distinguished with ".first()". Grrr ugly loop is needed.
    found = False
    for next in Note.objects.filter(datetime__lte=note.datetime).order_by(
        '-datetime', '-id'
    ):
        if found:
            return next
        if next == note:
            found = True


def note_and_next_hx(request, note_id):
    return HttpResponse(note_and_next_html(get_object_or_404(Note, pk=note_id)))
