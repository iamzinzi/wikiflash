#!/usr/bin/python3
""" pypi """
import wikipedia
from sys import argv


def main(a=argv[1], b=argv[2]):
    page1 = wikipedia.page(a)
    page2 = wikipedia.page(b)
    for l in page1.links:
        if l in page2.links:
            print(l)
        else:
            print("NO")


if __name__ == "__main__":
    main()