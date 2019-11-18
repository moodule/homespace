# -*- coding: utf-8 -*-

"""
===========
Smartphones
===========

Search for real-estate in ad listings.
"""

from __future__ import division, print_function, absolute_import

from homespace.items.smartphones import SmartphoneAd, SmartphoneAdLoader
from homespace.spiders._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

BRAND_VALUES = []

COLOR_VALUES = []

MODEL_VALUES = []

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100)))

#####################################################################
# FILTERS
#####################################################################

IRRELEVANT_ITEMS_FILTER = (
    '-fixe -fil -fax -minitel -talkie -montre -touche -vintage -gps'
    + ' -brassard -boite'
    + ' -ecouteur -kit -main -libre'
    + ' -rallonge -chargeur -adaptateur -cable -batterie'
    + ' -samsung -nokia -lumia -alcatel -logicom -motorola -asus -lg -jbl -siemens -doro'
    + ' -vitre -verre'
    + ' -pochette -coque -protection -support -housse -pied -perche -selfie -trepied -etui -protege')

#####################################################################
# SPIDER
#####################################################################

class SmartphonesSpider(LeboncoinSpider):
    name = 'smartphones'

    def __init__(self, *args, **kwargs):
        """
        """
        super(SmartphonesSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '17',
                'locations': '',
                'page': '1',
                'phone_brand': '',
                'phone_color': '',
                'phone_memory': '',
                'phone_model': '',
                'price': '',
                'shippable': '1',
                'text': IRRELEVANT_ITEMS_FILTER},
            'huawei': {
                'category': '17',
                'locations': '',
                'page': '1',
                'phone_brand': 'huawei',
                'phone_color': '',
                'phone_memory': '',
                'phone_model': '',
                'price': 'min-100',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'huawei ' + IRRELEVANT_ITEMS_FILTER}}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'brand': (
                '//div[contains(@data-qa-id, "criteria_item_phone_brand")]'
                + '/div/div[2]/text()'),
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_phone_color")]'
                + '/div/div[2]/text()'),
            'model': (
                '//div[contains(@data-qa-id, "criteria_item_phone_model")]'
                + '/div/div[2]/text()'),
            'ram': (
                '//div[contains(@data-qa-id, "criteria_item_phone_memory")]'
                + '/div/div[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = SmartphoneAd
        self._loader_class = SmartphoneAdLoader
