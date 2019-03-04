import factory
from . import models


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Author

    first_name = factory.Sequence(lambda n: 'john%s' % n)
    last_name = factory.Sequence(lambda n: 'smith%s' % n)