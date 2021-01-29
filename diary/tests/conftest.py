import pytest
from diary.models import Note


@pytest.fixture()
def note(db):
    return Note.objects.create(title='My Title', text='my text')

@pytest.fixture()
def note2(note):
    return Note.objects.create(title='My second', text='my second text')