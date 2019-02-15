#!/usr/bin/python3
""" test """
import requests
import json
import wikipedia
from sys import argv


def main(a=argv[1], b=argv[2]):
    S = requests.Session()

    URL1 = "https://en.wikipedia.org/w/api.php"
    Url2 = "https://en.wikipedia.org/w/api.php"
    PARAMS1 = {
        "action": "query",
        "format": "json",
        "titles": a,
        "prop": "links"
    }
    PARAMS2 = {
        "action": "query",
        "format": "json",
        "titles": b,
        "prop": "links"
    }
    R1 = S.get(url=URL1, params=PARAMS1)
    R2 = S.get(url=Url2, params=PARAMS2)
    DATA1 = R1.json()
    DATA2 = R2.json()
    # print(json.dumps(DATA1, indent=2))
    # print(json.dumps(DATA2, indent=2))
    print(DATA1.get("query").get("pages").get('19714').get('links'))
    print(DATA2.get("links"))
if __name__ == "__main__":
    main()
