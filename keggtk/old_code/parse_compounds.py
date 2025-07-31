import os
import pandas as pd

compfiles = os.listdir("data/compounds/")
formulas = {}
for filename in compfiles:
    file = open(f"data/compounds/{filename}", "r")
    lines = file.readlines()[0:-1]

    for line in lines:
        if line.split()[0] == "ENTRY":
            entry = line.split()[1]
            if entry in formulas.keys():
                print("DUPLICATE", entry)
        if line.split()[0] == "FORMULA":
            formula = line.split()[1]
            formulas[entry] = formula

df = pd.DataFrame([formulas])
df = df.transpose()
df.columns = ["formula"]
df["formula"].value_counts()

df[df["formula"] == "C6H13O9P"]
