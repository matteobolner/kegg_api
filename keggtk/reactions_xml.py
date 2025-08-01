import xml.etree.ElementTree as ET
import pandas as pd
import requests


def get_reactions_from_pathway(pathway_id):
    url = f"https://rest.kegg.jp/get/{pathway_id}/kgml"
    data = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(data.text))
    root = tree.getroot()

    entries = root.findall("entry")
    reaction_entries = root.findall("reaction")

    genes = []
    for e in entries:
        if e.get("type") == "gene":
            gene = {}
            gene["gene"] = e.get("name")
            gene["reaction"] = e.get("reaction")
            # symbols = e.findall("graphics")[0].get("name").split(",")[0]
            # gene["symbol"] = symbols.split(",")[0]
            genes.append(gene)

    genes = pd.DataFrame(genes)
    genes["gene"] = genes["gene"].str.split(" ")
    genes = genes.explode("gene")
    genes = genes.drop_duplicates()
    # genes = genes[genes["reaction"].notna()]

    reactions = []

    for r in reaction_entries:
        reaction = {}
        reaction["reaction"] = r.get("name")
        reaction["type"] = r.get("type")
        substrate = r.find("substrate").get("name")
        product = r.find("substrate").get("name")
        reaction["substrate"] = substrate
        reaction["product"] = product
        reactions.append(reaction)

    reactions = pd.DataFrame(reactions)
    reactions["reaction"] = reactions["reaction"].str.split(" ")
    reactions = reactions.explode("reaction")
    reactions = reactions.drop_duplicates()

    df = reactions.merge(genes, on="reaction", how="outer")
    return df
