# -*- coding: utf-8 -*-

"""
===============
Sports Gear Ads
===============

Items scraped from sports gear ads.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, TakeFirst
from scrapy import Field

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SPORTS
#####################################################################

class SportsGearAd(SecondHandAd):
    """
    """
    # Specifications
    pass

class SportsGearAdLoader(SecondHandAdLoader):
    """
    """
    pass
