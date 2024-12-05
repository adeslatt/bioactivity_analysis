import argparse
import sys
from bioactivity_analysis.fetch_pubchem import fetch_pubchem_bioactivity
from bioactivity_analysis.fetch_chembl import fetch_chembl_bioactivity
from bioactivity_analysis.utils import generate_summary, save_to_file


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Bioactivity Analysis Tool")
    parser.add_argument("uniprot_id", help="UniProt ID of the target protein.")
    parser.add_argument("--output", help="Base filename for saving data.", default="output")
    parser.add_argument("--format", help="Output format: json or yaml.", default="json", choices=["json", "yaml"])
    return parser.parse_args()


def main():
    """
    Entry point for the script.
    """
    # Check if running in a Jupyter notebook
    try:
        if get_ipython().__class__.__name__ == "ZMQInteractiveShell":
            print("Running inside a Jupyter Notebook.")
            return
    except NameError:
        pass

    # If not in a notebook, parse arguments
    args = parse_args()

    # Fetch data
    pubchem_bioactivity = fetch_pubchem_bioactivity(args.uniprot_id)
    chembl_bioactivity = fetch_chembl_bioactivity(args.uniprot_id)

    # Generate summaries
    pubchem_summary = generate_summary(pubchem_bioactivity)
    chembl_summary = generate_summary(chembl_bioactivity)

    # Prepare output
    output_data = {
        "PubChem": {
            "Bioactivity": pubchem_bioactivity,
            "Summary": pubchem_summary
        },
        "ChEMBL": {
            "Bioactivity": chembl_bioactivity,
            "Summary": chembl_summary
        }
    }

    # Save output
    output_file = f"{args.output}.{args.format}"
    save_to_file(output_data, output_file, format=args.format)
    print(f"Output saved to {output_file}")


if __name__ == "__main__":
    main()
