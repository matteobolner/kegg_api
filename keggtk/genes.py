import requests
from keggtk.parsing import parse_sections


def get_multiple_genes_text(gene_ids):
    url = "http://rest.kegg.jp/get/"
    current_url = url + "+".join(gene_ids)
    pathways = requests.get(current_url).text
    pathways_dict = {i: j for i, j in zip(gene_ids, pathways.split("///\n\n"))}
    return pathways_dict


def get_gene_symbols(text):
    parsed = parse_sections(text)
    return parsed["SYMBOL"][0].split(", ")


def get_db_links(text):
    parsed = parse_sections(text)
    dblinks = {i.split(": ")[0]: i.split(": ")[1] for i in parsed["DBLINKS"]}
    return dblinks
