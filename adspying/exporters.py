# -*- coding: utf-8 -*-

"""
===============
Items Exporting
===============

Export/serialize items into different formats.
"""

from __future__ import division, print_function, absolute_import

import io

from scrapy.exporters import BaseItemExporter, JsonItemExporter
from scrapy.utils.python import to_bytes, to_unicode

from adspying._wrangling import serialize_html_tag

#####################################################################
# HTML
#####################################################################

def serialize_html_table_row(
        values) -> str:
    """
    Enclose the items in an HTML table:
    - one column by attribute
    - one row by item

    Parameters
    ----------
    values: list.
        The list of items.

    Returns
    -------
    out: str.
        The serialized items.
    """
    return serialize_html_tag(
        tag='<tr>',
        value=''.join([serialize_html_tag(tag='<td>', value=str(v)) for v in values]))

class HtmlItemExporter(BaseItemExporter):

    def __init__(
            self,
            file,
            include_headers_line=True,
            join_multivalued=',',
            **kwargs):
        self._configure(kwargs, dont_fail=True)
        if not self.encoding:
            self.encoding = 'utf-8'
        self.include_headers_line = include_headers_line
        self.stream = io.TextIOWrapper(
            file,
            line_buffering=False,
            write_through=True,
            encoding=self.encoding,
            newline='') # Windows needs this https://github.com/scrapy/scrapy/issues/3034
        self._headers_not_written = True
        self._join_multivalued = join_multivalued

    def serialize_field(self, field, name, value):
        serializer = field.get('serializer', self._join_if_needed)
        return serializer(value)

    def _join_if_needed(self, value):
        if isinstance(value, (list, tuple)):
            try:
                return self._join_multivalued.join(value)
            except TypeError:  # list in value may not contain strings
                pass
        return value

    def start_exporting(self):
        self.stream.write('<table>')

    def finish_exporting(self):
        self.stream.write('</tbody></table>')

    def export_item(self, item):
        if self._headers_not_written:
            self._headers_not_written = False
            self._write_headers_and_set_fields_to_export(item)

        fields = self._get_serialized_fields(
            item,
            default_value='',
            include_empty=True)

        values = list(self._build_row(x for _, x in fields))

        self.stream.write(to_unicode(
            serialize_html_table_row(values),
            self.encoding))

    def _build_row(self, values):
        for s in values:
            try:
                yield to_unicode(s, self.encoding)
            except TypeError:
                yield s

    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                if isinstance(item, dict):
                    # for dicts try using fields of the first item
                    self.fields_to_export = list(item.keys())
                else:
                    # use fields declared in Item
                    self.fields_to_export = list(item.fields.keys())
            row = list(self._build_row(self.fields_to_export))
            self.stream.write(to_unicode(
                serialize_html_tag(
                    value=serialize_html_table_row(row),
                    tag='<thead>'),
                self.encoding))

        self.stream.write('<tbody>')

#####################################################################
# GEOJSON
#####################################################################

class GeoJsonItemExporter(JsonItemExporter):

    def start_exporting(self):
        self.file.write(b'{"type": "FeatureCollection", "features": [')
        self._beautify_newline()

    def finish_exporting(self):
        self._beautify_newline()
        self.file.write(b"]}")

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',')
            self._beautify_newline()


        __item_properties = dict(self._get_serialized_fields(item))

        __item = {
            'type': 'Feature',
            'properties': __item_properties,
            'geometry': {
                'type': 'Point',
                'coordinates': (
                    float(__item_properties.get('longitude', 0.0)),
                    float(__item_properties.get('latitude', 0.0)))}}

        self.file.write(to_bytes(
            self.encoder.encode(__item),
            self.encoding))
