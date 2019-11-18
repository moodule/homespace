# -*- coding: utf-8 -*-

"""
============
Computer Ads
============

Items scraped from informatics hardware ads.
"""

from __future__ import division, print_function, absolute_import

from scrapy import Field
from scrapy.loader.processors import Identity, Join, TakeFirst

from homespace.items._ad import SecondHandAd, SecondHandAdLoader

#####################################################################
# COMPUTER
#####################################################################

class ComputerAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = Field()
    ram_size = Field()

class ComputerAdLoader(SecondHandAdLoader):
    """
    """
    ram_model_in = Join()
    ram_model_out = Identity()

    ram_size_in = Join()
    ram_size_out = Identity()

class LaptopAd(SecondHandAd):
    """
    """
    # Specifications
    ram_model = Field()
    ram_size = Field()

class MotherBoardAd(SecondHandAd):
    """
    """
    # Specifications
    chipset = Field()
    bus = Field()
    size = Field()
    ethernet = Field()
    wifi = Field()
    graphics = Field()
    connections = Field()

class GraphicsCardAd(SecondHandAd):
    """
    """
    # Specifications
    gpu_frequency = Field()
    gpu_cores = Field()
    ram_frequency = Field()
    ram_size = Field()
    port = Field()
    connections = Field()

class HardDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class SolidStateDriveAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class RamAd(SecondHandAd):
    """
    """
    # Specifications
    speed = Field()
    size = Field()
    technology = Field()

class PowerSupplyAd(SecondHandAd):
    """
    """
    # Specifications
    power = Field()
    noise = Field()
    size = Field()

class CasingAd(SecondHandAd):
    """
    """
    # Specifications
    outside_size = Field()
    motherboard_size = Field()
    connections = Field()