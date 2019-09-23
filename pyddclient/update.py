"""Module for update function"""
import logging
import socket
import requests

from .urls import UPDATE_URL
from .util import get_public_address


def update(domain_name, username, password):
    """
    Look up the domain name and compare it against the public IP address.
    If they differ, update the IP address in Google Dynamic DNS and return
    True if successful.  Otherwise, return False.

    Raises OSError.
    """
    logging.info("evaluating domain %s", domain_name)

    public_address = get_public_address()
    logging.info("public IP address is %s", public_address)

    domain_address = socket.gethostbyname(domain_name)
    logging.info("domain IP address is %s", domain_address)

    if domain_address == public_address:
        logging.info("domain is up to date")
        return False

    logging.info("IP address mismatch, will attempt update")
    response = requests.post(
        url=UPDATE_URL,
        data={'hostname': domain_name, 'myip': public_address},
        auth=(username, password)
    )
    logging.info("response: %s %s", response.status_code, response.reason)

    if response.status_code == 200:
        if response.text.startswith('good'):
            return True
        elif response.text.startswith('nochg'):
            return False
        else:
            raise OSError(f"Update error: {response.text}")
    else:
        raise OSError(f"Request error: {response.reason}")
