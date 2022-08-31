# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from cleantext import clean
import glob

from vendorolx import settings


class PhonePipeline:
    def process_item(self, item, spider):
        if item["user_tlp"]:
            return item
        else:
            raise DropItem(
                item["user_name"] + " Doesn" + "'" + "t has" + " mobile number"
            )


class FilterPipeline:
    def process_item(self, item, spider):
        if (
            item["total_listing"] > 1 or item["lst_val"] < 30000000
        ):  # this is the logic to check if the user is a broker or an owner
            raise DropItem("Indicates broker or tempat kost: %s" % item["user_name"])
        else:
            return item


class DuplicatesPipeline:
    def process_item(self, item, spider):
        import pandas as pd

        clean_data = pd.read_csv("master.csv")
        if (item["user_url"] or item("user_tlp")) in clean_data.values:
            raise DropItem(
                "Duplicates item found: %s " % item["user_name"]
            )  # drop it if true
        else:
            return item


class CategoryPipeline:
    def process_item(self, item, spider):
        category_id = item["category_id"]
        item["category_id"] = self.check_category(category_id)
        return item

    def check_category(self, code):
        jenis = {
            "5158": "Dijual Rumah-Apartemen",
            "5160": "Disewakan Rumah-Apartemen",
            "4827": "Dijual Tanah",
            "4833": "Dijual Tempat Kos",
            "5154": "Dijual Bangunan Komersial",
            "5156": "Disewakan Bangunan Komersial",
        }
        result = jenis.get(code)
        return result


class CreateURLPipeline:
    def process_item(self, item, spider):
        title = item["title"]
        listing_id = item["listing_id"]
        item["title"] = clean(title, no_punct=True)
        title = title.replace("-", " ")
        title = title.replace("|", "")
        title = title.replace("/", "")
        title = title.replace(" ", "-")
        human_url = "https://www.olx.co.id/item/" + title + "-iid-" + listing_id + " "
        item["human_url"] = human_url
        return item


class WhatsappPipeline:
    def process_item(self, item, spider):
        user_tlp = item["user_tlp"]
        human_url = item["human_url"]
        message = (
            "Selamat siang, kenalkan saya Eka dari Kantor Properti Brighton Sanur, mau tanya iklan property di OLX ini:"
            + human_url
            + "apakah milik sendiri atau titipan? Kalau milik sendiri boleh saya bantu pasarkan ya?"
        )
        message = message.replace(" ", "%20")
        whatsapp_api = (
            "https://api.whatsapp.com/send?phone=" + str(user_tlp) + "&text=" + message
        )
        item["link_whatsapp"] = whatsapp_api
        return item
