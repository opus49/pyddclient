"""Module for utility functions"""

import requests
from .urls import EXTERNAL_SERVICE_URLS


def get_public_address():
    """Use an external service to determine public IP address."""
    for url in EXTERNAL_SERVICE_URLS:
        try:
            response = requests.post(url=url)
            if response.status_code == 200:
                return response.text.strip()
        except OSError:
            pass
    raise OSError("Could not determine public IP address.")
