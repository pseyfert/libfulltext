# copyright © 2017 the libfulltext authors (see AUTHORS.md and LICENSE)
"""American Physical Society publisher module"""

import requests


def get_aps_fulltext(doi, save_stream):
    """Retrieve APS fulltext

    Args:
        doi:         DOI string
        save_stream: function that saves a stream (arguments: stream, path)
    """
    response = requests.get(
        'http://harvest.aps.org/v2/journals/articles/{0}'.format(doi),
        headers={"Accept": "application/pdf"},
        stream=True
        )
    response.raise_for_status()

    save_stream(response, 'fulltext.pdf')
