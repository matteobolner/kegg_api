import requests


def get_genes_list(organism, get_pathway_file=False):
    url = "http://rest.kegg.jp/list/genes/" + organism
    data = requests.get(url)
    pathways = data.text
    pathways_text = data.text
    pathways = pathways.split("\n")
    pathways = filter(None, pathways)
    pathway_dict = dict()
    for path in pathways:
        path = path.split("\t")
        name = path[1]
        pathid = re.search(r"(.*)", path[0]).group(1)
        pathway_dict[pathid] = name
    if get_pathway_file:
        return pathway_dict, pathways_text
    else:
        return pathway_dict


organism = "hsa"
url = "http://rest.kegg.jp/list/genes/" + organism
data = requests.get(url)
