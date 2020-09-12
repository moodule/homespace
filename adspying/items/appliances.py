# -*- coding: utf-8 -*-

"""
==============
Appliances Ads
==============

Items scraped from appliances ads.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, TakeFirst
from scrapy import Field

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# APPLIANCES
#####################################################################

class AppliancesAd(SecondHandAd):
    """
    """
    # Specifications
    pass

class AppliancesAdLoader(SecondHandAdLoader):
    """
    """
    pass
