# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import argparse

#####################################################################
# CLI
#####################################################################

def main():
    """
    An alternative to the scrapy shell / scrapy crawl.
    Allows to launch several scraping jobs at once.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    parser = argparse.ArgumentParser(
        description='A toolbox to scrape second-hand ads.')
    parser.add_argument(
        '-s',
        '--spider',
        help='The spider to use for scraping.',
        required=False)

    args = parser.parse_args()

if __name__ == "__main__":
    main()
