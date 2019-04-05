from . import factories


def make_objects():
    do_nothing = True
    factories.AuthorFactory.create_batch(size=50)
