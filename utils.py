import json
import yaml
import matplotlib.pyplot as plt

def save_to_file(data, filename, format='json'):
    """
    Save data to a specified format (JSON or YAML).
    """
    with open(filename, "w") as file:
        if format == 'json':
            json.dump(data, file, indent=4)
        elif format == 'yaml':
            yaml.dump(data, file, sort_keys=False)
        else:
            raise ValueError("Unsupported format. Use 'json' or 'yaml'.")

def visualize_overlap(data1, data2, label1, label2):
    """
    Visualize overlaps between two datasets using a Venn diagram.
    """
    plt.figure(figsize=(6, 6))
    plt.title("Overlap Visualization")
    plt.gca().add_patch(plt.Circle((0.4, 0.5), 0.3, fill=False, label=label1))
    plt.gca().add_patch(plt.Circle((0.6, 0.5), 0.3, fill=False, label=label2))
    plt.legend()
    plt.show()
