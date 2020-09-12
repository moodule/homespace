# -*- coding: utf-8 -*-

"""
==============
smartphone Ads
==============

Items scraped from smartphones ads.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, TakeFirst
from scrapy import Field

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SMARTPHONES
#####################################################################

class SmartphoneAd(SecondHandAd):
    """
    """
    # Specifications
    os = Field()
    ram = Field()
    ssd = Field()
    battery = Field()
    camera = Field()
    size = Field()
    weight = Field()

class SmartphoneAdLoader(SecondHandAdLoader):
    """
    """
    os_in = Identity()
    os_out = Join()

    ram_in = Identity()
    ram_out = Join()
    
    ssd_in = Identity()
    ssd_out = Join()
    
    battery_in = Identity()
    battery_out = Join()
    
    camera_in = Identity()
    camera_out = Join()
    
    size_in = Identity()
    size_out = Join()
    
    weight_in = Identity()
    weight_out = Join()
