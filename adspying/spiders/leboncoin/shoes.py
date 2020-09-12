# -*- coding: utf-8 -*-

"""
=====
Shoes
=====

Search for shoes in ad listings.
"""

from __future__ import division, print_function, absolute_import

from adspying.items.shoes import ShoesAd, ShoesAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

CATEGORY_VALUES = {
    'baskets sneakers': 'basket',
    'chaussures lacets': 'lacet',
    'chaussures scratch': 'scratch',
    'mocassins': 'mocassin',
    'bottines lowboots': 'bottine',
    'bottes': 'botte',
    'escarpins': 'escarpin',
    'sandales nu-pieds': 'sandale',
    'chaussons pantoufles': 'chausson',
    'ballerines': 'ballerine',
    'autres': 'autre'
}

PRICE_VALUES = (
    list(range(0, 30, 5))
    + [40, 50, 100, 250])

SIZE_VALUES = {
    '41': '26' # eu: cm
}

TYPE_VALUES = {
    'women': '1',
    'men': '2',
    'children': '3'}

#####################################################################
# SPIDER
#####################################################################

class LeboncoinShoesSpider(LeboncoinSpider):
    name = 'leboncoin_shoes'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinShoesSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '53',
                'locations': '',
                'page': '1',
                'shippable': '1',
                'shoe_category_a': '',
                'shoe_size': '',
                'shoe_type': '',
                'price': '',
                'text': ''},
            'vans': {
                'category': '53',
                'locations': '',
                'page': '1',
                'search_in': 'subject',
                'shippable': '1',
                'shoe_category_a': '',
                'shoe_size': '26',
                'shoe_type': '',
                'price': 'min-100',
                'text': 'vans'}}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'category': (
                '//div[contains(@data-qa-id, "criteria_item_shoe_category")]'
                + '/div/div[2]/text()'),
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_clothing_color")]'
                + '/div/div[2]/text()'),
            'size': (
                '//div[contains(@data-qa-id, "criteria_item_shoe_size")]'
                + '/div/div[2]/text()'),
            # 'type': (
            #     '//div[contains(@data-qa-id, "criteria_item_shoe_type")]'
            #     + '/div/div[2]/text()'), # men / women, mostly useless
        }

        # classes to store, clean and export the data
        self._item_class = ShoesAd
        self._loader_class = ShoesAdLoader
