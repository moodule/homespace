# -*- coding: utf-8 -*-

"""
===========
Real-Estate
===========

Search for real-estate in ad listings.
"""

from __future__ import division, print_function, absolute_import

from adspying.items.realestate import RealEstateAd, RealEstateAdLoader
from adspying.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

PRICE_VALUES = (
    list(range(0, 375000, 25000))
    + list(range(400000, 700000, 50000))
    + list(range(700000, 1500000, 100000))
    + [1500000, 2000000])

ROOMS_VALUES = list(range(1, 9, 1))

SQUARE_VALUES = (
    list(range(20, 160, 10))
    + [200, 300, 500])

TYPE_VALUES = ['old', 'new', 'viager']

#####################################################################
# SPIDER
#####################################################################

class LeboncoinRealEstateSpider(LeboncoinSpider):
    name = 'leboncoin_realestate'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinRealEstateSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '9',
                'immo_sell_type': '',
                'locations': '',
                'owner_type': '', # private / pro
                'page': '1',
                'real_estate_type': '',
                'rooms': '',
                'shippable': '',
                'square': '',
                'price': '',
                'text': ''},
            'farmily': {
                'category': '9',
                'immo_sell_type': '',
                'locations': 'Saint-Etienne_42000__45.43988_4.39554_10000_50000',
                'page': '1',
                'real_estate_type': '1',
                'rooms': '2-max',
                'shippable': '',
                'square': '50-max',
                'price': 'min-350000',
                'text': '("jardin" OR "terrain" OR "potager") NOT "pas de jardin" NOT "ni jardin" NOT "sans jardin"'},
            'chulie': {
                'category': '10', # renting
                'immo_sell_type': '',
                'locations': 'd_54',
                'page': '1',
                'real_estate_type': '1,2',
                'rooms': '2-max',
                'shippable': '',
                'square': '40-max',
                'price': '300-700',
                'text': '("jardin" OR "terrain" OR "potager") NOT "pas de jardin" NOT "ni jardin" NOT "sans jardin"'},}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'category': (
                '//div[contains(@data-qa-id, "criteria_item_real_estate_type")]'
                + '/div[2]/p[2]/text()'),
            'energy_grade': (
                '//div[contains(@data-qa-id, "criteria_item_energy_rate")]'
                + '/div[2]/div[2]'
                + '/div[contains(@class, "styles_active__JYbKW")]/text()'),
            'fees_included': (
                '//div[contains(@data-qa-id, "criteria_item_charges_included")]'
                + '/div[2]/p[2]/text()'),
            'ghg_grade': (
                '//div[contains(@data-qa-id, "criteria_item_ges")]'
                + '/div[2]/div[2]'
                + '/div[contains(@class, "styles_active__JYbKW")]/text()'),
            'indoor_area': (
                '//div[contains(@data-qa-id, "criteria_item_square")]'
                + '/div[2]/p[2]/text()'),
            'rooms': (
                '//div[contains(@data-qa-id, "criteria_item_rooms")]'
                + '/div[2]/p[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = RealEstateAd
        self._loader_class = RealEstateAdLoader

        # context
        self._icon = 'veterinary'

        # export only relevant fields
        self.fields_to_export = [
            'url',
            'title',
            'category',
            'description',
            'location',
            'postal_code',
            'latitude',
            'longitude',
            'first_posted',
            'last_updated',
            'reposting_count',
            'age',
            'price',
            'starting_price',
            'price_per_square_meter',
            'indoor_area',
            'outdoor_area',
            'rooms',
            'fees_included',
            'energy_grade',
            'ghg_grade',
            'images',
            'time_to_work',
            'value_rating',
            'leverage_rating',
            'summary',
            'vendor']
