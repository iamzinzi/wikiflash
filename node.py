#!/usr/bin/python3
"""define data structure node
"""


class Node:
    """represent one page
    """

    def __init__(self, page, dist=0, prev=None):
        self.page, self.dist, self.prev = page, dist, prev
