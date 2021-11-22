import pytest
from html_form_to_dict import html_form_to_dict

from diary.models import Note
from diary.utils import HttpResponseUnprocessableEntity, HttpResponseCreated
from diary.views.note import get_next_or_none


def test_get_next_or_none__last(note):
    assert get_next_or_none(note) is None


def test_get_next_or_none__next_exists(note2):
    assert get_next_or_none(note2).title == 'My Title'

@pytest.mark.django_db
def test_start_page__invalid(client):
    response = client.get('/')
    assert response.status_code == 200
    data = html_form_to_dict(response.content)
    assert list(data.keys()) == ['datetime', 'initial-datetime', 'title', 'text']
    data['text'] = 'my text'
    response = data.submit(client)
    assert response.status_code == HttpResponseUnprocessableEntity.status_code
    assert response.description == ('<ul class="errorlist"><li>title<ul class="errorlist"><li>This field is '
                                    'required.</li></ul></li></ul>')

@pytest.mark.django_db
def test_start_page__valid(client):
    response = client.get('/')
    assert response.status_code == 200
    data = html_form_to_dict(response.content)
    data['text'] = 'my text'
    data['title'] = 'my title'
    response = data.submit(client)
    assert isinstance(response, HttpResponseCreated)
    note = Note.objects.get(id=response.pk)
    assert note.title == 'my title'
    assert note.text == 'my text'
