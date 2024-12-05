import json
import yaml

def generate_summary(data):
    """
    Generate a summary of IC50, Ki, and Kd ranges.
    """
    metrics = {"IC50": [], "Ki": [], "Kd": []}
    for entry in data:
        # Ensure standard_type and standard_value are valid
        if (
            'standard_type' in entry 
            and 'standard_value' in entry 
            and entry['standard_value'] is not None
        ):
            try:
                metrics[entry['standard_type']].append(float(entry['standard_value']))
            except (ValueError, TypeError):
                # Skip invalid or non-convertible values
                continue

    summary = {}
    for key, values in metrics.items():
        if values:
            summary[key] = {"min": min(values), "max": max(values)}
    return summary

def save_to_file(data, filename, format):
    """
    Save data to a file in JSON or YAML format.
    """
    with open(filename, "w") as file:
        if format == "json":
            json.dump(data, file, indent=4)
        elif format == "yaml":
            yaml.dump(data, file, sort_keys=False)
        else:
            raise ValueError("Unsupported format. Use 'json' or 'yaml'.")
