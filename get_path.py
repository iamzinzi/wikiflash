#!/usr/bin/python3
"""get shortest path from a wiki word to another
"""
import requests
import wikipedia
Node = __import__('node').Node

def is_place(place_name):
    """is_place takes a string argument, creates a wikipedia object,
    and checks if it's a city, state, or country. Returns True if string
    argument is a city, state, or country. False otherwise.
    """
    filters = ['city', 'state', 'country']

    try:
        place = wikipedia.page(place_name)
    except wikipedia.exceptions.DisambiguationError as e:
        place = wikipedia.page(e.options[0])
    first_paragraph = place.summary.split('\n')[0]
    for f in filters:
        if f in first_paragraph:
            return True
    return False

def validate(word):
    try:
        page = wikipedia.page(word)
    except:
        return False
    return True

def in_list(title, l):
    """check if a node title is in list
    """
    for node in l:
        if node.page.title == title:
            return True
    return False

def get_node(title, l):
    """get a node from a list
    """
    for node in l:
        if node.page.title == title:
            return node

def has_num(s):
    """check if string has number
    """
    return any([e.isdigit() for e in s])

def backref(node):
    """return list of tuples indicating path
    tuples are formatted as (title, url)
    """
    l = [(node.page.title, node.page.url)]
    while (node.prev):
        node = node.prev
        l.append((node.page.title, node.page.url))
    l.reverse()
    return l

def get_path(start, end):
    """get shortest part from start word to end word
    Arguments:
    start: start word
    end: end word
    Returns:
    dictionary: {"path": [(title, url), ...], "dist": distancs}
    returns empty dictionary if start or end is invalid
    """
    # validate start and end
    v1, v2 = validate(start), validate(end)
    if not v1 or not v2:
        if not v1 and not v2:
            return 3
        if not v1:
            return 1
        if not v2:
            return 2
    if start == end:
        page = wikipedia.page(start)
        return [(page.title, page.url)]
    start, end = Node(wikipedia.page(start)), Node(wikipedia.page(end))
    unv, v, ret = [start], [], None
    while (len(unv)):
        cur = unv[0]
        if cur.page.title == end.page.title:
            cur.prev = v[-1]
            ret = cur
            break
        # list of titles linked to cur
        links = cur.page.links
        # append and mark neighbors
        for link in links:
            if not in_list(link, v) and not in_list(link, unv):
                if not has_num(link) and not is_place(link):
                    try:
                        node = Node(wikipedia.page(link))
                        unv.append(node)
                        node.dist, node.prev = cur.dist + 1, cur
                    except:
                        pass
            elif not in_list(link, v):
                node = get_node(link, unv)
                if cur.dist + 1 < node.dist or not node.prev:
                    node.dist, node.prev = cur.dist + 1, cur
        # move cur from unv to v
        v.append(cur)
        if cur.page.url == end.page.url:
            ret = cur
        unv = unv[1:]
    return backref(ret) if ret else []



if __name__ == "__main__":
    print(get_path("Task (project management)", 'Project management'))
