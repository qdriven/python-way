# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     link_checker
   Description :
   Author :        patrick
   date：          2019/7/9
-------------------------------------------------
   Change Activity:
                   2019/7/9:
-------------------------------------------------
"""
from requests_html import HTMLSession

__author__ = 'patrick'


class LinkCheck:

    def __init__(self, main_url):
        self.main_url = main_url
        self.session = HTMLSession()
        self.result_map = set()

    def get_first_level_links(self):
        return self.get_all_links(self.main_url)

    def get_all_links(self, url):
        r = self.session.get(url=url, verify=False)
        return r.html.absolute_links

    def check_urls(self):
        links = self.get_first_level_links()
        print("total links:" + str(len(links)))
        for link in links:
            self._check_url(link)

    def _check_url(self, url):
        try:
            r = self.session.get(url)
            if r.status_code != 200:
                print("url " + url + " doesn't work")
                return
            # r.status_code
            links = self.get_all_links(url)

            if len(links) > 0:
                for link in links:  ## remove duplicated
                    if link.find("ont") != -1:
                        if link in self.result_map: continue
                        self.result_map.add(link)
                        print("checked url:" + link)
                        self._check_url(link)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    lc = LinkCheck("https://ontid.readme.io")
    lc.check_urls()
