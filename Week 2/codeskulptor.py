# coding=utf-8
"""
Codeskulptor auxiliary functions
"""


def file2url(filename):
    """
    Return a completed CodeSkulptor URL ressource from a short `filename`.

    Example given in the `CodeSkulptor documentation`_:
    `file2url('assets-Quick_fox.txt')`
    return
    `'http://codeskulptor-assets.commondatastorage.googleapis.com/assets-Quick_fox.txt'`

    .. _`CodeSkulptor documentation`: http://www.codeskulptor.org/docs.html#file2url

    :param filename: str

    :raise: ValueError if filename is in a incorrect format
                         (the good format is '^[a-zA-Z][a-zA-Z0-9]*[_-]')

    :return: str
    """
    from re import search

    m = search('^([a-zA-Z][a-zA-Z0-9]*)[_-]', filename)

    if m is None:
        raise ValueError("invalid filename: '{}'".format(filename))

    return ('http://codeskulptor-{}.commondatastorage.googleapis.com/{}'
            .format(m.group(1), filename))
