#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup
import requests as req
import lxml

def main():
    resp = req.get("https://pogoda.ngs.ru")

    soup = BeautifulSoup(resp.text, 'lxml')

    line = (soup.find("span", class_="value__main"))
    print(line.string)

if __name__ == '__main__':
    main()