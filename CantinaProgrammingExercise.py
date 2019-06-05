import json
import sys

with open("SystemViewController.json", "r") as JSONFile:
    exerciseData = JSONFile.read()
data = json.loads(exerciseData)

# print(data.items())
# print(len(data.items()))


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
    return ns.matches  # , ns.count


print(matchSelector("identifier", "rate", data))

"""
def parseSelector(input):
    if input[0] == ".":
        matchSelector("classNames", input[1:], data)



def echoInput(input, output):
    pass


#matchSelector("classNames", "columns", data)
if __name__ == "__main__":
    echoInput(input("Enter a selector: "), sys.stdout)
"""