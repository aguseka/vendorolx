# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VendorolxItem(scrapy.Item):
    # define the fields for your item here like:
    total_listing = scrapy.Field()
    user_url = scrapy.Field()
    user_name = scrapy.Field()
    user_id = scrapy.Field()
    user_tlp = scrapy.Field()
    category_id = scrapy.Field()
    propinsi = scrapy.Field()
    kabupaten = scrapy.Field()
    kecamatan = scrapy.Field()
    prop_addrs = scrapy.Field()
    listing_id = scrapy.Field()
    lst_val = scrapy.Field()
    tipe = scrapy.Field()
    lb = scrapy.Field()
    lt = scrapy.Field()
    lantai = scrapy.Field()
    kt = scrapy.Field()
    km = scrapy.Field()
    fasilitas = scrapy.Field()
    title = scrapy.Field()
    lantai = scrapy.Field()
    kepemilikan = scrapy.Field()
    human_url = scrapy.Field()
    proc_status = scrapy.Field()
    link_whatsapp = scrapy.Field()
    images = scrapy.Field()
    all_detail = scrapy.Field()
