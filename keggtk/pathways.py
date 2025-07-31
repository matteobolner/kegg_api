import requests
import re
from tqdm import tqdm
import time

# organism = "hsa"


def get_pathways_list(organism, get_pathway_file=False):
    url = "http://rest.kegg.jp/list/pathway/" + organism
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


def save_pathway_list(organism="hsa", outfile="all_pathways.txt"):
    pathway_dict, pathways = get_pathways_list(organism, get_pathway_file=True)
    with open(outfile, "w") as f:
        f.write(pathways)
    print(f"Saved to {outfile}")
    return pathway_dict


def get_multiple_pathways_text(pathway_ids):
    url = "http://rest.kegg.jp/get/"
    current_url = url + "+".join(pathway_ids)
    pathways = requests.get(current_url).text
    pathways_dict = {i: j for i, j in zip(pathway_ids, pathways.split("///\n\n"))}
    return pathways_dict


def save_all_pathways(organism, outdir="pathways"):
    pathway_dict = get_pathways_list(organism, get_pathway_file=False)
    pathway_ids = list(pathway_dict.keys())
    pathway_ids_split = [
        pathway_ids[i : i + 10] for i in range(0, len(pathway_ids), 10)
    ]

    for i in tqdm(pathway_ids_split):
        print(i)
        tempdict = get_multiple_pathways_text(i)
        for j in tempdict.keys():
            with open(f"{outdir}/{j}.txt", "w") as f:
                f.write(tempdict[j])
                print(j)
        time.sleep(5)
    print("Saved all pathways to : ", outdir)
