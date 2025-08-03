import requests
from keggtk.parsing import parse_sections
from tqdm import tqdm


def get_multiple_genes_text(gene_ids):
    url = "http://rest.kegg.jp/get/"
    all_genes_dict = {}
    gene_ids = list(set(gene_ids))
    # split in groups of 10 for API limits
    for gene_batch_indices in tqdm(range(0, len(gene_ids), 10)):
        current_url = url + "+".join(
            gene_ids[gene_batch_indices : gene_batch_indices + 10]
        )
        gene_batch_names = gene_ids[gene_batch_indices : gene_batch_indices + 10]
        genes = requests.get(current_url).text

        genes_dict = {
            name: gene_text
            for name, gene_text in zip(gene_batch_names, genes.split("///\n\n"))
        }
        all_genes_dict.update(genes_dict)
    return all_genes_dict


def get_gene_symbols(text):
    parsed = parse_sections(text)
    return parsed["SYMBOL"][0].split(", ")


def get_db_links(text):
    parsed = parse_sections(text)
    dblinks = {i.split(": ")[0]: i.split(": ")[1] for i in parsed["DBLINKS"]}
    return dblinks
