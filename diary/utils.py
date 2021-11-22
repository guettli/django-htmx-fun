from django.http import HttpResponse


class HttpResponseUnprocessableEntity(HttpResponse):
    description: str = ''

    def __init__(self, content=b'', description=None, **kwargs):
        assert description is not None, 'Please provide a description. For example form.errors'
        super().__init__(content, **kwargs)
        self.description = str(description)

    status_code = 422


class HttpResponseCreated(HttpResponse):
    pk: str = ''

    def __init__(self, content=b'', pk=None, **kwargs):
        assert pk is not None, 'Please provide a pk (primary key) if the object which got saved'
        super().__init__(content, **kwargs)
        self.pk = pk

    status_code = 201
