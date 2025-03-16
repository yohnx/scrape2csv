from selectolax.parser import Node, HTMLParser
from typing import Union

def parse_raw_attribute(node: Node, selectors: list):
    parsed={} 
    for s in selectors: 
        match=s.get("match") 
        type=s.get("type")
        name=s.get("name")
        selector=s.get("selector")

        if match == "all":
            matched=node.css(selector)
            if type == "text":
                parsed[name]=[node.text() for node in matched]
            if type=="node":
                parsed[name]=matched
        elif match == "first":
            matched=node.css_first(selector)
            if type=="text":
                parsed[name]=matched.text()
            elif type=="node":
                parsed[name]=matched
    return parsed
