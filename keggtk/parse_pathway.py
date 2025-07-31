import os
import requests
import sys
from tqdm import tqdm


# file = open(sys.argv[1], "r")
file = open("data/pathways/hsa00630.txt", "r")
rawtext = file.read()  # .rstrip("///\n")
lines = rawtext.split("\n")
print(rawtext)

cpds_start = [lines.index(i) for i in lines if i.startswith("COMPOUND")][0]
reference_start = [
    lines.index(i)
    for i in lines
    if i.startswith("REFERENCE") or i.startswith("REL_PATHWAY")
][0]
complist = []

cpds_lines = lines[cpds_start:reference_start]
first_cpd = cpds_lines.pop(0).split()[1]
complist.append(first_cpd)
complist = complist + [i.split()[0] for i in cpds_lines]

base_url = "http://rest.kegg.jp/get/"

compounds_split = [complist[i : i + 10] for i in range(0, len(complist), 10)]

for i in tqdm(compounds_split):
    print(i)
    temp_compounds = requests.get(base_url + "+".join(i)).text
    for j in temp_compounds.split("///\n\n"):
        print(j)
        tempname = j.split()[1]
        print(tempname)
        if os.path.exists(f"data/compounds/{tempname}.txt"):
            pass
        else:
            with open(f"data/compounds/{tempname}.txt", "wb") as f:
                f.write(j.encode("utf-8"))
