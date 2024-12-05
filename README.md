# bioactivity_analysis


bioactivity_analysis/

├── bioactivity_analysis/       # Main package directory
│   ├── __init__.py             # Marks as a Python package
│   ├── core.py                 # Core logic for fetching data
│   ├── utils.py                # Helper functions (e.g., file saving, visualization)
│   ├── main.py                 # Entry point for CLI and notebook detection
│   └── notebook_detect.py      # Jupyter notebook detection logic
├── tests/                      # Unit test directory
│   ├── __init__.py             # Marks as a Python package
│   ├── test_core.py            # Unit tests for core.py
│   └── test_utils.py           # Unit tests for utils.py
├── docs/                       # Sphinx documentation directory
│   ├── conf.py                 # Sphinx configuration
│   ├── index.rst               # Main documentation index
│   └── Makefile                # For building docs locally
├── .github/
│   └── workflows/
│       └── test.yml            # GitHub Actions for testing
├── environment.yml             # Conda environment file
├── requirements.txt            # Additional pip dependencies
├── README.md                   # Project README
└── setup.py                    # Installation script


## Features

###Command-Line Arguments:

1. Specify the target UniProt ID and optional file output base name:

```bash
python bioactivity_script.py P00734 --output bioactivity_comparison
```

2. Modularity:

Each function focuses on a single task (fetching bioactivity, extracting GO terms, saving to CSV, visualizing overlaps).

3. Unit Testing:

Validates key functionalities like fetching PubChem and ChEMBL data and extracting GO terms.

Run tests with:

```bash
python -m unittest script.py
```

4.  Venn Diagram Visualization:

Illustrates the overlap between PubChem and ChEMBL bioactivity data.


5.  CSV Outputs:

Saves bioactivity and GO term data into CSV files for further analysis.

```bash
bioactivity_comparison_pubchem_bioactivity.csv
bioactivity_comparison_chembl_bioactivity.csv
bioactivity_comparison_pubchem_go_terms.csv
bioactivity_comparison_chembl_go_terms.csv
```

## Relationship Between PubChem and ChEMBL

### PubChem Imports ChEMBL Data:

PubChem periodically ingests data from ChEMBL. This includes compound information, bioactivity data, and assay results.
ChEMBL data in PubChem is tagged with a source identifier (e.g., ChEMBL Target, ChEMBL Compound).

### ChEMBL Data in PubChem:

ChEMBL data in PubChem can often be incomplete, outdated, or missing some specific bioactivity details found directly in ChEMBL.
PubChem tends to aggregate data from multiple sources (ChEMBL, BindingDB, DrugBank, etc.), which can create redundancy or inconsistency.

### No Live Synchronization:

Unlike the synchronization seen in SRA and EGA (which share infrastructure for genomic data), PubChem and ChEMBL maintain separate pipelines and databases.
Changes in ChEMBL (e.g., new targets, updated IC50 values) are not immediately reflected in PubChem until the next scheduled import.

### Key Differences Between PubChem and ChEMBL

 | Feature | PubChem | ChEMBL |
 | ------  | ------  | ------ |
 | Primary Focus | General chemical and bioactivity data aggregation. | Bioactivity data with a focus on drug discovery. |
 | Data Sources	| Aggregates from ChEMBL, DrugBank, BindingDB, etc. | Manually curated from literature and experiments. |
 | Uniprot Integration | Target-centric, manually curated mappings. | Broad automated UniProt linkage |
 | GO Terms | GO slim terms curated for pharmacology | General GO terms from aggregated data. |
 | Target Coverage | Broader coverage but less detail for some targets. | Highly curated, detailed target information. |
 | Bioactivity Data | Sometimes lacks assay conditions or binding details. | Detailed, includes assay types, binding metrics. |



