---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: 1.3
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Bioactivity Data Analysis with PubChem and ChEMBL

This notebook provides an interactive way to explore bioactivity data for a specific protein target using UniProt IDs.
This is a notebook to show protein bioActivity accessible from PubChem and ChEMBL to show what data can be derived from these sites and compare and contrast the results.

---

## Setup



```python
import requests
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from chembl_webresource_client.new_client import new_client
import unittest
```

Define all the modules to fetch the bioactivity data from PubChem and ChEMBL

```python
# Module: Fetch data from PubChem
def fetch_pubchem_bioactivity(uniprot_id):
    """
    Fetch bioactivity data from PubChem for a given UniProt ID.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/protein/{uniprot_id}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('Table', {}).get('Row', [])
    else:
        return []

# Module: Fetch data from ChEMBL
def fetch_chembl_bioactivity(uniprot_id):
    """
    Fetch bioactivity data from ChEMBL for a given UniProt ID.
    """
    target = new_client.target.filter(target_components__accession=uniprot_id)
    targets = list(target)
    if not targets:
        return []
    
    target_chembl_id = targets[0]['target_chembl_id']
    activities = new_client.activity.filter(
        target_chembl_id=target_chembl_id,
        standard_type__in=["IC50", "Ki", "Kd"]
    )
    return list(activities)


# Module: Extract GO terms
def extract_chembl_go_terms(uniprot_id):
    """
    Extract GO terms from ChEMBL for a given UniProt ID.
    """
    target = new_client.target.filter(target_components__accession=uniprot_id)
    targets = list(target)
    if not targets:
        return []
    
    go_terms = targets[0].get('component_go_slim', [])
    return go_terms


def extract_pubchem_go_terms(uniprot_id):
    """
    Extract GO terms from PubChem for a given UniProt ID.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/protein/{uniprot_id}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        description = response.json()
        return description.get('Table', {}).get('GO_Terms', [])
    else:
        return []


# Module: Save data to CSV
def save_to_csv(data, filename):
    """
    Save data to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


# Module: Visualization
def visualize_overlap(data1, data2, label1, label2, title):
    """
    Visualize overlaps between two datasets using a Venn diagram.
    """
    set1 = set(data1)
    set2 = set(data2)
    plt.figure(figsize=(6, 6))
    plt.title(title)
    plt.gca().add_patch(plt.Circle((0.5, 0.5), 0.3, fill=False, label=label1))
    plt.gca().add_patch(plt.Circle((0.7, 0.5), 0.3, fill=False, label=label2))
    plt.legend()
    plt.show()

```

Enter Target Protein

```python
# Interactive Input
uniprot_id = input("Enter UniProt ID for the target protein: ")

```

```python
# Fetch data
pubchem_bioactivity = fetch_pubchem_bioactivity(uniprot_id)
# Show counts
print(f"PubChem: Retrieved {len(pubchem_bioactivity)} bioactivity records.")

```

```python


```

```python
print(f"ChEMBL : Retrieved {len(chembl_bioactivity)} bioactivity records.")
print(f"PubChem: Retrieved {len(pubchem_go_terms)} pubchem_go_terms.")
print(f"ChEMBL : Retrieved {len(chembl_go_terms)} chembl_go_terms.")
```

```python
# Visualize results
visualize_overlap(
   [d['CID'] for d in pubchem_bioactivity if 'CID' in d],
   [d['molecule_chembl_id'] for d in chembl_bioactivity if 'molecule_chembl_id' in d],
   "PubChem",
   "ChEMBL",
   "Bioactivity Overlap"
)
```

```python

# Save results to CSV
save_to_csv(pubchem_bioactivity, f"{args.uniprot_id_pubchem_bioactivity.csv")
save_to_csv(chembl_bioactivity, f"{args.uniprot_id}_chembl_bioactivity.csv")
save_to_csv(pubchem_go_terms, f"{args.uniprot_id}_pubchem_go_terms.csv")
save_to_csv(chembl_go_terms, f"{args.uniprot_id}_chembl_go_terms.csv")


```

```python
if __name__ == "__main__":
    main()

```
