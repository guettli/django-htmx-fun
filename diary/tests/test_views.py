from diary.views import get_next_or_none
from django.urls import reverse


def test_get_next_or_none__last(note):
    assert get_next_or_none(note) is None

def test_get_next_or_none__next_exists(note2):
    assert get_next_or_none(note2).title == 'My Title'

def test_NoteListView(client, note):
    response = client.get(reverse('note-list'))
    assert response.status_code == 200
    assert b'<div hx-get="/note/create" hx-trigger="load" hx-swap="outerHTML"></div>' in response.content
