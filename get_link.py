#!/usr/bin/python3
"""python3 get_link.py <title>
"""


import sys
import requests


def get_link():
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": sys.argv[1],
        "prop": "links",
        "pllimit": "max",
    }
    dic = {}
    R = S.get(url=URL, params=PARAMS)
    D = R.json()['query']['pages']
    num = list(D.keys())[0]
    DATA = D[num]['links']
    for item in DATA:
        temp = "_".join(item['title'].split())
        dic[temp] = "https://en.wikipedia.org/wiki/" + temp
    print(dic)
    return(dic)

get_link()
