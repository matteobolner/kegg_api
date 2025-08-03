from keggtk.utils import parse_sections
from tqdm import tqdm


def get_gene_symbols(text):
    parsed = parse_sections(text)
    return parsed["SYMBOL"][0].split(", ")


def get_db_links(text):
    parsed = parse_sections(text)
    dblinks = {i.split(": ")[0]: i.split(": ")[1] for i in parsed["DBLINKS"]}
    return dblinks
