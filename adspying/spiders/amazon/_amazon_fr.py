# -*- coding: utf-8 -*-

"""
======
Amazon
======

Base class for scraping amazon.

The scraped data is compiled into a referential to complete the
data scraped from other websites.

Every child class customize the meta to fit a specific ad search:
- query args
- ad attributes (price, size, condition, whatever)
- data selectors (for the attributes specific to this type of ads)

For example, an appliance ad will specify the "condition" of the 
item while a real-estate ad has no use for such an attribute.

But all ads are layed out in a similar way, in HTML.
"""

from __future__ import division, print_function, absolute_import

from urllib.parse import urlencode, urljoin

import scrapy

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader
from adspying.spiders._secondhandads import SecondHandAdsSpider

#####################################################################
# SPIDER
#####################################################################

class AmazonSpider(SecondHandAdsSpider):
    name = 'amazon'
    allowed_domains = ['www.amazon.fr']

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(self, *args, **kwargs):
        """
        """
        super(AmazonSpider, self).__init__(*args, **kwargs)

        # stop condition
        self._max_pages = 1
        self._max_age = 1 # in days

        # url template
        self._base_url = 'https://www.amazon.fr/'
        self._search_page_url = '/s?{}'

        # forge a url to query amazon
        self._current_query_name = 'default'
        self._current_query_args = {}
        self._queries = {
            'default': {
                'bbn': '',
                'i': '', # (sub)category??
                'k': '', # search text
                'page': '',
                'rh': '',}}

        #############################################################
        # AD LISTING DATA SELECTION
        #############################################################
        self._ad_listing_xpath = ''
        self._ad_listing_attributes_xpath = {
            'images': '',
            'title': '',
            'price': '',
            'location': '',
            'last_updated': '',
            'url': '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a',}


        #############################################################
        # AD PAGE DATA SELECTION
        #############################################################
        self._ad_xpath = ''
        self._ad_generic_attributes_xpath = {
            'images': '',
            'title': '',
            'price': '',
            'condition': '',
            'last_updated': '',
            'location': '',
            'description': '',}

        # select data specific to a given ad search (say smartphones)
        self._ad_specific_attributes_xpath = {} # intended to be overriden by the subclass

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader
