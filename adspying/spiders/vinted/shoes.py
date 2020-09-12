# -*- coding: utf-8 -*-

"""
======
Vinted
======

Derived class for specialized searches of shoes.
"""

from __future__ import division, print_function, absolute_import

from adspying.spiders.vinted._vinted import VintedSpider

#####################################################################
# SPIDER
#####################################################################

class VintedShoesSpider(VintedSpider):
    name = 'vinted_shoes'

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(VintedShoesSpider, self).__init__(*args, **kwargs)

        self._search_page_url = '/hommes/chaussures?{}'

        # forge a url to query vinted
        self._current_query_name = 'default'
        self._current_query_args = {}
        self._queries = {
            'default': {
                'page': '1',
                'price_to': '100',
                'brand_id[]': '6055',
                'size_id[]': '784',},
            'scarpa_42':{
                'page': '1',
                'price_to': '100',
                'brand_id[]': '6055',
                'size_id[]': '784',},
            'sportiva_42':{
                'page': '1',
                'price_to': '100',
                'brand_id[]': '201320',
                'size_id[]': '784',},}
