import xml.etree.ElementTree as ET
import pandas as pd
import requests


def get_reactions_from_pathway(pathway_id):
    url = f"https://rest.kegg.jp/get/{pathway_id}/kgml"
    data = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(data.text))
    root = tree.getroot()
    entries = root.findall("entry")
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
    genes["reaction"] = genes["reaction"].str.split(" ")
    genes = genes.explode("reaction")
    genes = genes.drop_duplicates()
    # genes = genes[genes["reaction"].notna()]
    reaction_entries = root.findall("reaction")
    reactions = []

    for r in reaction_entries:
        reaction = {}
        reaction["reaction"] = r.get("name")
        reaction["type"] = r.get("type")
        substrate = r.find("substrate").get("name")
        product = r.find("product").get("name")
        reaction["substrate"] = substrate
        reaction["product"] = product
        reactions.append(reaction)
    reactions = pd.DataFrame(reactions)
    if len(reactions) > 0:
        reactions["reaction"] = reactions["reaction"].str.split(" ")
        reactions = reactions.explode("reaction")
        reactions["substrate"] = reactions["substrate"].str.split(" ")
        reactions = reactions.explode("substrate")
        reactions["product"] = reactions["product"].str.split(" ")
        reactions = reactions.explode("product")
        reactions = reactions.drop_duplicates()
        df = reactions.merge(genes, on="reaction", how="outer")
        return df
    else:
        return genes
