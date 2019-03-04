from . import factories


def make_objects():
    factories.AuthorFactory.create_batch(size=50)