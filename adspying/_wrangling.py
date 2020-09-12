# -*- coding: utf-8 -*-

"""
==============
Data Wrangling
==============

Clean the raw data scraped from the web.
"""

from __future__ import absolute_import, division, print_function

from bs4 import BeautifulSoup
from datetime import datetime
from nltk.metrics.distance import edit_distance
import re
import unicodedata

#####################################################################
# CONSTANTS
#####################################################################

ANY_AREA_REGEX = '(\d+)\s*(?:m²|m2|metres?\ carres?)?'
OUTDOOR_AREA_REGEX = '(?:terrain|jardin|parc)\s*(?:de)?\s*' + ANY_AREA_REGEX
PRICE_REGEX = '([-+]?[0-9]*\.?[0-9]+)'

#####################################################################
# ENCODING & FORMAT
#####################################################################

def format_datetime(
        string: str,
        format: str) -> str:
    """
    Mold any serialized datetime to the ISO-8601 format.

    Example:
        27/02/2020 8:42
        => 2020-02-27T08:42:00

    Parameters
    ----------
    string: str.
        A serialized datetime.
    format: str.
        Location of the relevant datetime values in the input string.

    Returns
    -------
    out: str.
        The serialized datetime with ISO-8601 format '%Y-%m-%dT%H:%M:%S'.
    """
    return datetime.strptime(
        string,
        format).isoformat(sep='T', timespec='seconds')

def format_text(
        text: str) -> str:
    """
    Remove duplicate spacing and convert to lower case.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        The formated text.
    """
    return remove_extra_spacing(remove_accents(text.lower()))

def format_number(
        text: str) -> float:
    """
    Convert strings to float.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: float.
        The formated text.
    """
    __as_text = format_text(text)
    __is_a_number = re.search(
        '([-+]?[0-9]+\.?[0-9]*).*',
        format_text(text))
    if __is_a_number:
        return float(__is_a_number.group(1))
    else:
        return None

#####################################################################
# TEXT
#####################################################################

def remove_accents(
        text: str) -> str:
    """
    Replace all the accented character with regular characters.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        The closest string without accents.
    """
    nfkd_form = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def remove_all_spacing(
        text: str) -> str:
    """
    Remove all the spaces in a string.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        The string without spaces.
    """
    return ''.join(text.split())

def remove_extra_spacing(
        text: str) -> str:
    """
    Replace any spacing by a single whitspace.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        A lean version of the input.
    """
    return ' '.join(text.split())

def remove_special_characters(
        text: str) -> str:
    """
    Replace all the special characters by '_'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: str.
        A safe version of the input.
    """
    return re.sub(
        '\W+',
        '',
        text)

#####################################################################
# HTML
#####################################################################

def extract_text_from_html_markup(
        html: str) -> str:
    """
    Extract the text *visible* to a user on an internet browser,
    from a string of html markup.
    The chunks of text are separated by newlines.

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The visible text.
    """
    __soup = BeautifulSoup(markup=html, features="lxml")

    # kill all script and style elements
    for script in __soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    __text = __soup.get_text(separator='.')

    # break into lines and remove leading and trailing space on each
    __lines = (
        __line.strip()
        for __line in __text.splitlines())
    # break multi-headlines into a line each
    __chunks = (
        __phrase.strip()
        for __line in __lines
        for __phrase in __line.split("."))
    # drop blank lines
    return '\n'.join(
        __chunk
        for __chunk in __chunks if __chunk)

def prettify_html(
        html: str) -> str:
    """
    Expand the html markup formatting:
    - break lines on opening tags
    - indent lines

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The beautified html.
    """
    return BeautifulSoup(
        markup=html,
        features="lxml").prettify()

def serialize_html_tag(
        tag: str,
        value: str = '',
        attributes: dict = {}) -> str:
    """
    Serialize any tag as a string.

    Parameters
    ----------
    tag: str.
        The HTML tag type.
    value: str.
        The text enclosed in the tag.

    Returns
    -------
    out: str.
        The serialized HTML tag.
    """
    return '{}{}{}'.format(
        tag.replace(
            '>',
            ' ' + ' '.join(['{}="{}"'.format(k, v) for k, v in attributes.items()]) + '>'),
        value,
        tag.replace('<', '</'))

#####################################################################
# DATA MINING
#####################################################################

def extract_area_value(
        text: str) -> int:
    """
    Extract the numeric value of an area in a string like '102 m²'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: int.
        A positive value of there's a match, -1 otherwise.
    """
    area_matches = re.search(ANY_AREA_REGEX, text, re.IGNORECASE)

    if area_matches:
        return int(area_matches.group(1))
    else:
        return -1

def extract_price_value(
        text: str) -> int:
    """
    Extract the numeric value of a price in a string like '320 €'.

    Parameters
    ----------
    text: str.
        Any chunk of text.

    Returns
    -------
    out: int.
        A positive value of there's a match, -1 otherwise.
    """
    area_matches = re.search(PRICE_REGEX, text, re.IGNORECASE)

    if area_matches:
        return int(float(area_matches.group(1)))
    else:
        return -1
