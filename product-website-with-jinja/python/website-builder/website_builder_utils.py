import json
from jinja2 import Environment, FileSystemLoader

PRODUCT_INPUT_FOLDER = "product-data"
OUTPUT_FOLDER = "../../website"

env = Environment(loader=FileSystemLoader("templates"))

def load_json(path):
    # Illustrate basic use of built-in "json" library to load a JSON file into a Python dictionary (or array)
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_text_file(output_path, text_string):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text_string)
