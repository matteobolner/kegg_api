import re


def extract_sections(pathway_file):
    file = open(pathway_file, "r")
    rawtext = file.read().rstrip("\n")
    sections = {}
    for i in rawtext.split("\n"):
        if i[:3] == "///":
            continue
        section = i[:12].strip()
        section_data = i[12:].strip()
        if section != "":
            section_name = section
            if section_name not in sections.keys():
                sections[section_name] = []
        sections[section_name].append(section_data)
    # for k, v in sections.items():
    #    if len(v) == 1:
    #        sections[k] = v[0]
    return sections


sections = extract_sections("data/pathways/hsa04931.txt")


def split_id_and_name(line):
    if len(line.split()) > 1:
        return {line.split()[0]: line.split(" ", 1)[1]}
    else:
        return {line: ""}


def split_gene_info(line):
    pattern = (
        r"^\s*(\d+)\s+([^;]+);\s*([^\[]+)\s*(?:\[KO:([^\]]+)\])?\s*(?:\[EC:([^\]]+)\])?"
    )
    match = re.match(pattern, line)
    if match:
        gene_id, symbol, name, ko, ec = match.groups()
        return {
            "id": gene_id,
            "symbol": symbol,
            "name": name,
            "ko": ko,
            "ec": ec,
        }


entry = [split_id_and_name(i) for i in sections["ENTRY"]]
pathway_map = [split_id_and_name(i) for i in sections["PATHWAY_MAP"]]
network = [split_id_and_name(i) for i in sections["NETWORK"]]
network_element = [split_id_and_name(i) for i in sections["ELEMENT"]]
drugs = [split_id_and_name(i) for i in sections["DRUG"]]
compounds = [split_id_and_name(i) for i in sections["COMPOUND"]]
gene_info = [split_gene_info(i) for i in sections["GENE"]]

for i in sections.keys():
    print(i)


class KEGGPathway:
    def __init__(
        self,
        entry,
        name,
        description,
        pathway_class,
        pathway_map,
        network,
        drugs,
        organism,
        genes,
        compounds,
        references,
        rel_pathways,
        ko_pathway,
    ):
        self.entry = entry
        self.name = name
        self.description = description
        self.pathway_class = pathway_class
        self.pathway_map = pathway_map
        self.network = network
        self.drugs = drugs
        self.organism = organism
        self.genes = genes
        self.compounds = compounds
        self.references = references
        self.rel_pathways = rel_pathways
        self.ko_pathway = ko_pathway
