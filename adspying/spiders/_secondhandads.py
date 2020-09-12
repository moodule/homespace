# -*- coding: utf-8 -*-

"""
=====================
Second Hand Ad Spider
=====================

Base class for scraping second hand listings.

It defines the overall querying process:
1) search the webservice for ads
2) crawl the listing pages to get the ads' urls
3) scrape each individual ad informations

The actual queries are defined in the subclasses, since it depends:
- on the item of interest
- and on the webservice being searched
"""

from __future__ import division, print_function, absolute_import

from urllib.parse import urlencode, urljoin

import scrapy

from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# SPIDER
#####################################################################

class SecondHandAdsSpider(scrapy.Spider):
    """
    Base class for scraping second hand listings.

    It defines the overall querying process:
    1) search the webservice for ads
    2) crawl the listing pages to get the ads' urls
    3) scrape each individual ad informations

    The actual queries are defined in the subclasses, since it all
    depends on the item of interest and the webservice searched.
    """
    name = 'second_hand_ads'
    project = 'adspying'

    #################################################################
    # CLI
    #################################################################

    def _select_current_query(
            self):
        """
        Select the query to be executed.
        """
        self._current_query_name = getattr(
            self,
            'query',
            'default')
        self._current_query_args = self._queries.get(self._current_query_name)

    def _fill_current_query_args_with_cli_args(
            self):
        """
        Merge the default query arguments with those given through the cli.
        """
        for __key, __value in self._current_query_args.items():
            self._current_query_args[__key] = getattr(
                self,
                __key,
                __value) # default to the current value

    def _set_stop_conditions(
            self):
        """
        Define the stopping conditions:
        - after x pages of listing
        - when the listed ads get older than y
        """
        self._max_pages = int(getattr(
            self,
            'pages',
            '1'))

    #################################################################
    # CRAWLING METHODS
    #################################################################

    def __init__(
            self,
            *args,
            **kwargs):
        """
        Fill all the crawling parameters with default values.
        """
        super(SecondHandAdsSpider, self).__init__(*args, **kwargs)

        # stop condition
        self._max_pages = 1
        self._max_age = 1 # in days

        # url template
        self._base_url = ''
        self._search_page_url = ''

        # forge a query
        self._queries = {}
        self._current_query_name = 'default'
        self._current_query_args = {}

        # select data specific to a given ad search (say smartphones)
        self._ad_listing_xpath = ''
        self._ad_listing_attributes_xpath = {}
        self._ad_xpath = ''
        self._ad_generic_attributes_xpath = {}
        self._ad_specific_attributes_xpath = {}

        # classes to store, clean and export the data
        self._item_class = SecondHandAd
        self._loader_class = SecondHandAdLoader

        # context
        self._domain = ''
        self._datetime_format = '%Y-%m-%dT%H:%M:%S'
        self._icon = 'marker'

        # enable specific pipelines
        self._pipelines = ['MongoDbPipeline']

    def start_requests(
            self):
        """
        Query the webservice with an ad search.
        """
        # translate the cli args to the url std for leboncoin
        self._set_stop_conditions()
        self._select_current_query()
        self._fill_current_query_args_with_cli_args()

        # forge the search urls & queue the requests
        for i in range(self._max_pages):
            self._current_query_args['page'] = str(i + 1)
            yield scrapy.Request(
                url=urljoin(
                    self._base_url,
                    self._search_page_url.format(urlencode(self._current_query_args))),
                callback=self.parse_listing,
                meta={
                    'page': str(i+1),
                    'dont_redirect': True})

    def parse_listing(
            self,
            response):
        """
        Parse the listing of ads returned by the webservice:
        - retrieve the url of each individual ad
        - follow each link to scrape the detailed informations
        """
        __page = response.meta.get(
            'page',
            '1')
        __ad_links = response.xpath(
            self._ad_listing_xpath).xpath(
            self._ad_listing_attributes_xpath['url']).getall()

        for __link in __ad_links:
            yield scrapy.Request(
                url=urljoin(self._base_url, __link),
                callback=self.parse_item,
                meta={
                    'dont_redirect': True})

        self.log('[Page {page}] {count} ads queued...'.format(
            page = __page,
            count = len(__ad_links)))

    def parse_item(
            self,
            response):
        """
        Parse the detailed information available in the webpage
        of a given ad.

        Use the specific xpath defined in the subclasses. 
        """
        # select only the part of the page dedicated to the ad
        # ie discard header, menus etc
        __loader = self._loader_class(
            item=self._item_class(),
            selector=response.xpath(self._ad_xpath))

        # used to convert datetime from webservice format to ISO 8601
        __loader.context['datetime_format'] = self._datetime_format

        # used to mark the location of the ad on a map
        __loader.context['icon'] = self._icon

        # used to prepend to url postfixes
        __loader.context['base_url'] = self._base_url

        # used to display the source of an item (after data aggregation)
        __loader.context['domain'] = self._domain

        __loader.add_value('url', response.url)

        # scrape generic ad attributes
        for __field, __xpath in self._ad_generic_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        # scrape attributes specific to given type of ad (say real-estate)
        for __field, __xpath in self._ad_specific_attributes_xpath.items():
            __loader.add_xpath(__field, __xpath)

        return __loader.load_item()
