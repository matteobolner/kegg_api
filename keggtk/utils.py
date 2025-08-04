import requests
from tqdm import tqdm
import pandas as pd
import io


def list_db_ids(database, organism=""):
    url = f"http://rest.kegg.jp/list/{database}/" + organism
    data = requests.get(url)
    data = data.text
    df = pd.read_table(io.StringIO(data.rstrip("\n")), header=None)
    return df


def download_multiple_ids_text(ids):
    url = "http://rest.kegg.jp/get/"
    all_ids_dict = {}
    ids = list(set(ids))
    # split in groups of 10 for API limits
    for batch_indices in tqdm(range(0, len(ids), 10)):
        current_url = url + "+".join(ids[batch_indices : batch_indices + 10])
        batch_names = ids[batch_indices : batch_indices + 10]
        text_results = requests.get(current_url).text

        genes_dict = {
            name: text for name, text in zip(batch_names, text_results.split("///\n\n"))
        }
        all_ids_dict.update(genes_dict)
    return all_ids_dict


def parse_sections(text):
    """
    Parse KEGG pathway text into sections
    TODO: better parsing for BRITE and other layered sections
    """
    sections = {}
    for i in text.split("\n"):
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
