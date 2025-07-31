from dataclasses import dataclass


def parse_compound_text(text):
    lines = text.split("\n")
    attributes = {}
    for line in lines:
        line_elements = line.split()
        attr_title = line_elements[0]
        attr_values = line_elements[1:]
        if len(line) > 0:
            if line[0] != "///":
                attributes[line[0]] = line[1:]
                print(line[0], line[1:])
    return attributes


text = open("testdata/C02104.txt", "rb")
text = text.read()
text = text.decode("utf-8")


text = text.read()
text.split("\n")


with open("testdata/C02104.txt", "rb") as f:
    print(parse_compound_text(f.read().decode("utf-8")))


@dataclass
class KEGGCompound:
    entry: str
    name: list[str]
    formula: str
    remark: str
    comment: str
    reaction: list[str]
    pathway: list[str]
    module: list[str]
    network: list[str]
    enzimes: list[str]
    brite: list[str]
    dblinks: dict[str, str]
