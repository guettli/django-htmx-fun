from diary.models import Note
from django.contrib import admin


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ['id', 'datetime', 'title', 'text']
    ordering = ['-datetime', '-id']


admin.site.register(Note, NoteAdmin)
