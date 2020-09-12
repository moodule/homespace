# -*- coding: utf-8 -*-

"""
=========
Computers
=========

Search for computers in ad listings:
- desktop computers
- laptops
- hardware & parts
"""

from __future__ import division, print_function, absolute_import

from adspying.items.informatics import ComputerAd, ComputerAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100)))

#####################################################################
# SPIDER
#####################################################################

class LeboncoinComputersSpider(LeboncoinSpider):
    name = 'leboncoin_computers'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinComputersSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '15',
                'locations': '',
                'page': '1',
                'price': '',
                'search_in': '',
                'shippable': '1',
                'text': ''},
            'ssd': {
                'category': '15',
                'locations': '',
                'page': '1',
                'price': 'min-60',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'ssd'},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = ComputerAd
        self._loader_class = ComputerAdLoader
