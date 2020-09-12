# -*- coding: utf-8 -*-

"""
===========
Smartphones
===========

Search for smartphones in ad listings.
"""

from __future__ import division, print_function, absolute_import

from adspying.items.smartphones import SmartphoneAd, SmartphoneAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

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

class LeboncoinSmartphonesSpider(LeboncoinSpider):
    name = 'leboncoin_smartphones'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSmartphonesSpider, self).__init__(*args, **kwargs)

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
                'price': 'min-50',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'huawei ' + IRRELEVANT_ITEMS_FILTER},
            'pieces': {
                'category': '17',
                'locations': '',
                'page': '1',
                'phone_brand': '',
                'phone_color': '',
                'phone_memory': '',
                'phone_model': '',
                'price': 'min-30',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'pieces ' + IRRELEVANT_ITEMS_FILTER},
            'casse': {
                'category': '17',
                'locations': '',
                'page': '1',
                'phone_brand': '',
                'phone_color': '',
                'phone_memory': '',
                'phone_model': '',
                'price': 'min-30',
                'search_in': 'subject',
                'shippable': '1',
                'text': 'casse ' + IRRELEVANT_ITEMS_FILTER},}

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
