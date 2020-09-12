# -*- coding: utf-8 -*-

"""
============
Vehicule Ads
============

Items scraped from vehicule ads.
"""

from __future__ import division, print_function, absolute_import

from itemloaders.processors import Identity, Join, TakeFirst
from scrapy import Field

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# UTILITY VEHICULES
#####################################################################

class VehiculeAd(SecondHandAd):
    """
    """
    # Specifications
    fuel = Field()
    gearbox = Field()
    issuance = Field()
    mileage = Field()
    consumption = Field()
    size_inside = Field()
    size_outside = Field()

class VehiculeAdLoader(SecondHandAdLoader):
    """
    """
    # Specifications
    fuel_in = Identity()
    fuel_out = Join()

    gearbox_in = Identity()
    gearbox_out = Join()

    issuance_in = Identity()
    issuance_out = Join()

    mileage_in = Identity()
    mileage_out = Join()

    consumption_in = Identity()
    consumption_out = Join()

    size_inside_in = Identity()
    size_inside_out = Join()

    size_outside_in = Identity()
    size_outside_out = Join()

