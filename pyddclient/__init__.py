"""
Update dynamic DNS using Google API
"""
from .update import update
from .util import get_public_address

__all__ = ['get_public_address', 'update']
