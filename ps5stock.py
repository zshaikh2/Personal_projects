#! /usr/bin/env python
import urllib3
import time
from lxml import etree
from termcolor import colored

while(1):
    url = 'https://www.nowinstock.net/computers/videocards/amd/rx6800xt/'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    data = r.data
    stock = etree.HTML(data).xpath('//td')
    stock_rows = iter(reversed(stock))

    info_row = None
    for row in (stock_rows):

        if (isinstance(row.text,str)):
            if (row.text.find('-') == -1):
                info_row = row
        else:
            for i in row:
                if (info_row.text.find("Out of Stock") != -1):
                    print(colored(i.text,'red'), end='')
                    print(info_row.text)
                elif (info_row.text.find("In Stock") != -1):
                    print(colored(i.text, 'green'), end='')
                    print(info_row.text)
                else:
                    print(colored(i.text, 'blue'), end='')
                    print(info_row.text)

    print('-----------------------------------------------------------------')
    time.sleep(10)

