# -*- coding: utf-8 -*-

"""
=========
Pipelines
=========

Exporting data.
"""

from __future__ import division, print_function, absolute_import

from copy import deepcopy
from datetime import datetime, timedelta
from functools import wraps
from inspect import getfullargspec
import os

from pymongo import MongoClient
from scrapy.exporters import CsvItemExporter
from scrapy.loader import ItemLoader

from adspying.exporters import GeoJsonItemExporter, HtmlItemExporter
from adspying.items._secondhandad import SecondHandAd, SecondHandAdLoader

#####################################################################
# ENABLE / DISABLE PIPELINES
#####################################################################

def _redirects_open_spider(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "open_spider" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    @wraps(pipeline_method)
    def open_spider_wrapper(self, spider):
        if self.__class__.__name__ in spider._pipelines:
            return pipeline_method(self, spider)
        else:
            return None
    return open_spider_wrapper

def _redirects_close_spider(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "close_spider" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    return _redirects_open_spider(pipeline_method)

def _redirects_process_item(
        pipeline_method: callable) -> callable:
    """
    Redirects to an empty "process_item" method,
    as replacement when the pipeline is not enabled for the current spider.
    """
    @wraps(pipeline_method)
    def process_item_wrapper(self, item, spider):
        if self.__class__.__name__ in spider._pipelines:
            return pipeline_method(self, item, spider)
        else:
            return item
    return process_item_wrapper

def redirects(
        pipeline_method: callable) -> callable:
    """
    This decorator turns pipeline methods on/off depending
    on the current spider.

    In practice, it replaces the wrapped method with an
    empty one if the conditions are not met.
    """
    if pipeline_method.__name__ == 'open_spider':
        return _redirects_open_spider(pipeline_method)
    elif pipeline_method.__name__ == 'close_spider':
        return _redirects_close_spider(pipeline_method)
    elif pipeline_method.__name__ == 'process_item':
        return _redirects_process_item(pipeline_method)

    return pipeline_method

#####################################################################
# BASE
#####################################################################

class BasePipeline(object):

    def __init__(
            self,
            parent_path,
            file_name,
            file_extension='.txt'):
        """
        Initiate the output according to the calling spider.
        """
        self._file_path = os.path.join(
            parent_path,
            file_name + file_extension)
        self._file = None

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
        __project_name = 'adspying'
        __spider_name = 'default'
        __query_name = 'default'
        if crawler.spider:
            __project_name = getattr(
                crawler.spider,
                'project',
                'adspying')
            __spider_name = getattr(
                crawler.spider,
                'name',
                'default')
            __query_name = getattr(
                crawler.spider,
                'query',
                'default')
            fields_to_export = getattr(
                crawler.spider,
                'fields_to_export',
                None)

        return cls(
            parent_path=os.path.join(
                os.path.realpath(
                    crawler.settings.get('EXPORT_FOLDER_PATH')),
                __project_name,
                __query_name.replace('_', '-')),
            file_name=__spider_name)

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        if getattr(self, '_file_path', ''):
            self._file = open(self._file_path, 'wb')

    @redirects
    def close_spider(
            self,
            spider):
        """
        """
        if getattr(self, 'exporter', None):
            self.exporter.finish_exporting()
        if (getattr(self, '_file', None) and not self._file.closed):
            self._file.close()

    @redirects
    def process_item(
            self,
            item,
            spider):
        """
        """
        if getattr(self, 'exporter', None):
            self.exporter.export_item(item)
        return item

#####################################################################
# CSV
#####################################################################

class CsvPipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(CsvPipeline, self).__init__(parent_path, file_name, '.csv')

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        super(CsvPipeline, self).open_spider(spider)
        if self._file:
            self.exporter = CsvItemExporter(
                file=self._file,
                delimiter=',',
                join_multivalued=' ',
                include_headers_line=True)
            self.exporter.start_exporting()

#####################################################################
# HTML
#####################################################################

class HtmlTablePipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        Save the output in an html file.

        Parameters
        ----------
        parent_path:

        Returns
        -------
        """
        super(HtmlTablePipeline, self).__init__(parent_path, file_name, '.html')

    @redirects
    def open_spider(
            self,
            spider):
        """
        Serialize using the HTML table exporter.
        """
        super(HtmlTablePipeline, self).open_spider(spider)
        if self._file:
            self.exporter = HtmlItemExporter(
                file=self._file,
                join_multivalued=' ',
                include_headers_line=True)
            self.exporter.start_exporting()

#####################################################################
# JSON
#####################################################################

class JsonPipeline(BasePipeline):

    def __init__(
            self,
            parent_path,
            file_name):
        """
        """
        super(JsonPipeline, self).__init__(parent_path, file_name, '.json')

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        super(JsonPipeline, self).open_spider(spider)
        if self._file:
            self.exporter = GeoJsonItemExporter(
                file=self._file)
            self.exporter.start_exporting()

#####################################################################
# MONGODB
#####################################################################

def  _interpret_serialized_data(
        item: dict) -> dict:
    """
    """
    __new_item = deepcopy(item)

    __new_item['first_posted'] = datetime.fromisoformat(item.get(
        'first_posted',
        datetime.now().isoformat(sep='T', timespec='seconds')))

    __new_item['last_updated'] = datetime.fromisoformat(item.get(
        'last_updated',
        datetime.now().isoformat(sep='T', timespec='seconds')))

    return __new_item

def _update_item_data(
        old_item: dict,
        new_item: dict) -> dict:
    """
    Process the timeline of the scraped data.
    The previous versions are not simply overwritten: it keeps track
    of the price and reposting evolution over time.

    Parameters
    ----------
    old_item: dict.
        The item already stored in the database.
    new_item: dict.
        The online version of the item, on the last scraping.

    Returns
    -------
    out: dict.
        The current item data, with the overall timeline.
    """
    __updated_item = deepcopy(new_item)

    # first posted: kept from the oldest record
    __updated_item['first_posted'] = old_item.get(
        'first_posted',
        new_item.get(
            'first_posted',
            datetime.now()))

    # age: from the oldest post
    __updated_item['age'] = (
        datetime.now()
        - __updated_item.get(
            'first_posted',
            datetime.now())).days

    # history of reposting
    if old_item.get('url', '') == new_item.get('url', ''):
        __updated_item['reposting_count'] = old_item.get('reposting_count', 0)
    else:
        __updated_item['reposting_count'] = old_item.get('reposting_count', 0) + 1

    # price delta since the first post
    __updated_item['starting_price'] = old_item.get(
        'starting_price',
        old_item.get(
            'price',
            new_item.get(
                'price',
                0)))

    return __updated_item

def _update_or_insert(
        collection,
        filter,
        item):
    """
    """
    if collection.count_documents(filter):
        collection.update_one(
            filter=filter,
            update={
                '$set': _update_item_data(
                    _interpret_serialized_data(collection.find_one(filter)),
                    _interpret_serialized_data(item))})
    else:
        collection.insert_one(dict(item))

class MongoDbPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection='default'):
        self._mongo_db_uri = mongo_uri
        self._mongo_db_name = mongo_db
        self._mongo_db_collection = mongo_collection

    @classmethod
    def from_crawler(
            cls,
            crawler):
        """
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017/'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'adspying')
        )

    @redirects
    def open_spider(
            self,
            spider):
        """
        """
        self._mongo_client = MongoClient(self._mongo_db_uri)
        self._mongo_db_collection = getattr(
            spider,
            'query',
            getattr(
                spider,
                'name',
                'default'))

        if self._mongo_client:
            self._mongo_db = self._mongo_client[self._mongo_db_name]

    @redirects
    def close_spider(
            self,
            spider):
        """
        """
        if self._mongo_client:
            self._mongo_client.close()

    @redirects
    def process_item(
            self,
            item,
            spider):
        """
        """
        if self._mongo_db:
            __url = item.get('url', '')
            __collection = self._mongo_db[self._mongo_db_collection]
            if __url:
                _update_or_insert(
                    __collection,
                    {
                        'vendor': item.get('vendor', ''),
                        'location': item.get('location', '')},
                    item)
            else:
                __collection.insert_one(dict(item))

        return item
