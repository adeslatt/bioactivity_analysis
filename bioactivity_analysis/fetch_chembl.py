from chembl_webresource_client.new_client import new_client

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
