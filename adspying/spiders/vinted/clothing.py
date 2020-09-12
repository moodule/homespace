# -*- coding: utf-8 -*-

"""
======
Vinted
======

Derived class for specialized searches of clothing.
"""

from __future__ import division, print_function, absolute_import

from adspying.spiders.vinted._vinted import VintedSpider

#####################################################################
# SPIDER
#####################################################################

class VintedClothingSpider(VintedSpider):
    name = 'vinted_clothing'

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(VintedClothingSpider, self).__init__(*args, **kwargs)

        self._search_page_url = '/hommes?{}'

        # forge a url to query vinted
        self._current_query_name = 'default'
        self._queries = {
            'default': {
                'brand_id[]': '209084',
                'page': '1',
                'price_to': '100',
                'size_id[]': '207',},
            'polaire_s':{
                'brand_id[]': '209084',
                'page': '1',
                'price_to': '100',
                'size_id[]': '207',},
            'veste_hardshell_s':{
                'brand_id[]': '209084',
                'page': '1',
                'price_to': '150',
                'size_id[]': '207',},}
