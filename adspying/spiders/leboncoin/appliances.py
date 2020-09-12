# -*- coding: utf-8 -*-

"""
====================
Leboncoin Appliances
====================

Search for appliances in ad listings.
"""

from __future__ import division, print_function, absolute_import

from adspying.items.appliances import AppliancesAd, AppliancesAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    [0, 5]
    + list(range(10, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100)))

#####################################################################
# SPIDER
#####################################################################

class LeboncoinAppliancesSpider(LeboncoinSpider):
    name = 'leboncoin_appliances'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinAppliancesSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '20',
                'locations': '',
                'page': '1',
                'price': '',
                'shippable': '1',
                'text': ''},
            'sewing_machine': {
                'category': '20',
                'locations': '',
                'page': '1',
                'price': '',
                'shippable': '1',
                'text': 'machine coudre'},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = AppliancesAd
        self._loader_class = AppliancesAdLoader
