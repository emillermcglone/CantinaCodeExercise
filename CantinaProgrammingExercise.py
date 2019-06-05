#!/usr/bin/env python3.7

import json
import sys

with open("SystemViewController.json", "r") as JSONFile:
    exerciseData = JSONFile.read()
    data = json.loads(exerciseData)


def matchingViews(attribute, selector, d):
    """ Find matching views based on the selector """

    class NameSpace(object):
        pass
    ns = NameSpace()
    ns.matches = []

    def inner(attribute, selector, d):
        for key, value in d.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        inner(attribute, selector, item)
                    elif key == attribute and item == selector:
                        ns.matches.append(d)
            elif isinstance(value, dict):
                inner(attribute, selector, value)
            elif key == attribute and value == selector:
                ns.matches.append(d)

    inner(attribute, selector, d)
    return ns.matches


def parseSelector(selector):
    """ Determine the view attribute from the selector """
    if selector[0] == ".":
        result = matchingViews("classNames", selector[1:], data)
    elif selector[0] == "#":
        result = matchingViews("identifier", selector[1:], data)
    else:
        result = matchingViews("class", selector, data)
    return result


def echoInput(selector, output):
    "Echo input to command line"
    selector = selector.strip('\"')
    result = json.dumps(parseSelector(selector))
    output.write(result)


if __name__ == "__main__":
    while True:
        echoInput(input("\nEnter a selector: "), sys.stdout)
