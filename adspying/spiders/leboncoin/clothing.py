# -*- coding: utf-8 -*-

"""
===========
Sports Gear
===========

Search for sports gear items in ad listings.
"""

from __future__ import division, print_function, absolute_import

from adspying.items.sports_gear import SportsGearAd, SportsGearAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100))
    + [1000])

#####################################################################
# FILTERS
#####################################################################

HARDSHELL_FILTER = ('')
SOFTSHELL_FILTER = ('')

#####################################################################
# SPIDER
#####################################################################

class LeboncoinClothingSpider(LeboncoinSpider):
    name = 'leboncoin_clothing'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinClothingSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '22',
                'clothing_st': '2', # size S
                'clothing_tag': '', # sport, manteau
                'clothing_type': '3', # men
                'locations': '',
                'page': '1',
                'price': '',
                'search_in': '',
                'shippable': '1',
                'text': ''},
            'mammut': {
                'category': '22',
                'clothing_st': '2', # size S
                'clothing_type': '3', # men
                'page': '1',
                'price': 'min-150',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'mammut'},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = SportsGearAd
        self._loader_class = SportsGearAdLoader
