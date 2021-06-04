from diary.views.note import get_next_or_none
from django.urls import reverse


def test_get_next_or_none__last(note):
    assert get_next_or_none(note) is None

def test_get_next_or_none__next_exists(note2):
    assert get_next_or_none(note2).title == 'My Title'

def test_start_page(client, note):
    response = client.get('/')
    assert response.status_code == 200
