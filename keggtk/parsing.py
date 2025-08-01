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
