import json
import sys

with open("SystemViewController.json", "r") as JSONFile:
    exerciseData = JSONFile.read()
data = json.loads(exerciseData)


def matchSelector(attribute, selector, d):

    class NameSpace(object):
        pass
    ns = NameSpace()
    ns.count = 0
    ns.matches = []

    def inner(attribute, selector, d):
        for key, value in d.items():
            # if value is a list
            if isinstance(value, list):
                # recurse through list items
                for item in value:
                    # if list items are a dictionary, recurse
                    if isinstance(item, dict):
                        inner(attribute, selector, item)
                    # if item is not a dictionary
                    elif key == attribute and item == selector:
                        ns.count += 1
                        ns.matches.append(d)
            # if value is a dict
            elif isinstance(value, dict):
                inner(attribute, selector, value)
            # check if key/value matches the attribute and selector
            elif key == attribute and value == selector:
                ns.count += 1
                ns.matches.append(d)

    inner(attribute, selector, d)
    return ns.matches


def parseSelector(input):
    """ Determine the view attribute """
    if input[0] == ".":
        result = matchSelector("classNames", input[1:], data)
    elif input[0] == "#":
        result = matchSelector("identifier", input[1:], data)
    else:
        result = matchSelector("class", input, data)
    return result


def echoInput(input, output):
    result = json.dumps(parseSelector(input))
    output.write(result)


#matchSelector("classNames", "columns", data)
if __name__ == "__main__":
    while True:
        echoInput(input("\nEnter a selector: "), sys.stdout)
