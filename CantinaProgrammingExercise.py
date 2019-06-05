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


def parseSelector(input):
    """ Determine the view attribute from the input """
    if input[0] == ".":
        result = matchingViews("classNames", input[1:], data)
    elif input[0] == "#":
        result = matchingViews("identifier", input[1:], data)
    else:
        result = matchingViews("class", input, data)
    return result


def echoInput(input, output):
    "Echo input to command line"
    result = json.dumps(parseSelector(input))
    output.write(result)


if __name__ == "__main__":
    while True:
        echoInput(input("\nEnter a selector: "), sys.stdout)
