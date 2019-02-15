#!/usr/bin/python3
"""python3 get_link.py <title>
"""


import sys
import requests


def get_link(link=sys.argv[1], dic={}, plcontinue=""):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": link,
        "prop": "links",
        "pllimit": "max",
    }
    if plcontinue != "":
        PARAMS['plcontinue'] = plcontinue
    R = S.get(url=URL, params=PARAMS)
    Json_Data = R.json()
    D = Json_Data['query']['pages']
    page_id = list(D.keys())[0]
    DATA = D[page_id]['links']
    for item in DATA:
        temp = "_".join(item['title'].split())
        dic[item['title']] = "https://en.wikipedia.org/wiki/" + temp
    if 'continue' in Json_Data.keys():
        plcontinue = Json_Data['continue'].get('plcontinue')
        return get_link(link, dic, plcontinue)
    else:
        return(dic)

#test
step1 = get_link()
try:
    print(step1['Continent'])
except:
    print("Can not find Continent")
step2 = get_link('Continent')
try:
    print(step2['Antarctica'])
except:
    print("Can not find Antarctica")
step3 = get_link('Antarctica')
try:
    print(step3["Mikhail Lazarev"])
    print("OK")
except:
    print("Can not find Mikhail Lazarev")
