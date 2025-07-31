from dataclasses import dataclass
from token import COMMENT



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


@dataclass
class KEGGReaction:
    entry: str
    name: str
    definition: str
    equation: str
    rclass: str
    enzyme: list[str]
    pathway: list[str]
    module: list[str]
    brite: list[str]
    orthology: str
    dblinks: dict[str, str]


@dataclass
class KEGGModule:
    entry: str
    name: str
    definition: str
    orthology: str
    module_class: str
    pathway: list[str]
    reaction: list[str]
    compound: list[str]
    comment: str
    reference: dict[str, str]



@dataclass
class Metabolite:
    ids: dict[str, str]
    name: list[str]
    formula: str
    reaction: list[str]
    pathway: list[str]
    module: list[str]
    network: list[str]
    enzimes: list[str]
    brite: list[str]



class ReactionEquation(substrates:list(KEGGCompound), products:list(KeggCompound)):
