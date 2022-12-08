# -*- coding: utf-8 -*-
import json
import re
import scrapy
from scrapy.http.request import Request
from cleantext import clean
from ..items import VendorolxItem


class Olx2Spider(scrapy.Spider):
    name = "olx2"
    allowed_domains = ["olx.co.id"]
    notbdg_dps = ["4000223", "4000222", "4000221", "5000007", "5000021", "4000219"]
    bdg_dps = ["4000225", "4000217"]
    gianyar_klungkung = [
        "4000223",
        "5000021",
    ]
    bali = [
        "4000223",  # klungkung
        "4000224",  # tabanan
        "4000222",  # karangasem
        "4000221",  # jembrana
        "5000007",  # bangli
        "5000021",  # gianyar
        "4000219",  # buleleng
        "4000225",  # denpasar
        "4000217",  # badung
    ]
    jkt = [
        "4000028",
        "4000030",
        "4000031",
        "4000032",
        "4000029",
    ]
    sby = ["4000216"]  # kode kota surabaya
    mks = ["4000307"]  # kode kota makassar
    mdn = ["4000131"]  # kode kota medan
    kal = ["4000266", "4000250", "4000279"]
    erma = [
        "4000216",
        "4000131",
        "4000266",
        "4000250",
        "4000279",
    ]

    categories = ["5158", "5160", "5154", "5156", "4827", "4833"]
    agent_name = "Eka"

    def start_requests(self):
        for location in self.bdg_dps:  # sedang membaca badung dan denpasar "bdg_dps"
            for category in self.categories:

                url = (
                    "https://www.olx.co.id/api/relevance/search?category="
                    + category
                    + "&facet_limit=100&location="
                    + location
                    + "&location_facet_limit=20&page=0"
                )
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fp_data = {}  # initiate a dictionary
        front_page = json.loads(response.text)  # loading the url response
        # get the data part from the json response
        listings = front_page["data"]
        for listing in listings:
            user_id = listing[
                "user_id"
            ]  # get the user id of all listings from the front page
            listing_id = listing["id"]  # get the id of the listing,
            # generate the url out of the listing_id
            url_listing = "https://www.olx.co.id/api/items/" + str(listing_id)
            # generate the api url out of the user_id, for the machine to read
            url_vendor = (
                "https://www.olx.co.id/api/v2/users/" + str(user_id) + "/items?limit=36"
            )
            fp_data["listing_id"] = listing_id
            fp_data["url_listing"] = url_listing
            fp_data["user_id"] = user_id

            # calling another function to parse the total listing
            request = scrapy.Request(
                url=url_vendor, callback=self.user_parse, cb_kwargs=fp_data
            )
            yield request
        try:
            next_url = front_page["metadata"][
                "next_page_url"
            ]  # check if next page is available
            if next_url:
                # looping to get another page
                yield Request(url=next_url, callback=self.parse)
        except KeyError:
            print("All pages has been crawled")

    # define the new function with data from previous function passed
    # pay attention variables being passed here are the key of dictionary not the value

    def user_parse(self, response, listing_id, url_listing, user_id):
        jlh_lst = {}  # initiate a dictionary
        # loading the user listing detail
        user_page = json.loads(response.text)
        total_listing = len(user_page["data"])  # get all listing of the user
        lst_val = user_page["data"][0]["price"]["value"]["raw"]
        # generate the non-api url (human readable)
        user_url = "https://www.olx.co.id/profile/" + str(user_id)
        # from this line below, is mean to save all data into dictionary
        jlh_lst["user_url"] = user_url
        jlh_lst["total_lst"] = total_listing
        jlh_lst["lst_val"] = lst_val
        jlh_lst["user_id"] = user_id
        data = scrapy.Request(
            url=url_listing,
            callback=self.parse_data,
            cb_kwargs=jlh_lst,
        )
        yield data

    # again, the one that is passed is the key of the dictionary
    def parse_data(self, response, user_url, total_lst, lst_val, user_id):
        all_data = VendorolxItem()
        listing_page = json.loads(response.text)
        all_data["category_id"] = listing_page["data"]["category_id"]
        all_data["user_id"] = listing_page["data"]["user_id"]
        all_data["title"] = listing_page["data"]["title"]
        all_data["total_listing"] = total_lst
        all_data["lst_val"] = lst_val
        all_data["listing_id"] = listing_page["data"]["id"]
        all_data["user_name"] = listing_page["metadata"]["users"][user_id]["name"]
        all_data["user_url"] = user_url
        all_data["proc_status"] = "just crawled"
        all_data["lst_val"] = listing_page["data"]["price"]["value"]["raw"]
        all_detail = listing_page["data"]["parameters"]
        this_id = {}
        for detail in all_detail:
            # extract the detail from dictionary. See the json result to understand this
            # put the key/value pair into the dictionary
            this_id[detail["key_name"]] = detail["value_name"]
            # use the function below to get the result
            all_data["prop_addrs"] = self.check_parameter("Alamat lokasi", this_id)
            all_data["user_tlp"] = self.check_parameter("phone", this_id)
            all_data["proc_status"] = "just crawled"
            all_data["tipe"] = self.check_parameter("Tipe", this_id)
            all_data["lb"] = self.check_parameter("Luas bangunan", this_id)
            all_data["lt"] = self.check_parameter("Luas tanah", this_id)
            all_data["kt"] = self.check_parameter("Kamar tidur", this_id)
            all_data["km"] = self.check_parameter("Kamar Mandi", this_id)
            all_data["fasilitas"] = self.check_parameter("Fasilitas", this_id)
            all_data["lantai"] = self.check_parameter("Lantai", this_id)
            all_data["kepemilikan"] = self.check_parameter("Sertifikasi", this_id)

        yield all_data

    def check_parameter(self, key, param_lst={}):
        try:
            hasil = param_lst.get(key)
            return hasil
        except:
            return "Null"

    # def response_is_ban(self, request, response):
    #    return b"banned" in response.body

    # def exception_is_ban(self, request, exception):
    #    return None
