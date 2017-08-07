# -*- coding: utf-8 -*-
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except (TypeError, ValueError):
    __version__ = 'unknown'
