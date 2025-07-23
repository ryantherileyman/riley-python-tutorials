import argparse
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

INPUT_FOLDER = "page-data"
OUTPUT_FOLDER = "output"

env = Environment(loader=FileSystemLoader("templates"))

def load_json(path):
    # Illustrate basic use of built-in "json" library to load a JSON file into a Python dictionary (or array)
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_text_file(output_path, text_string):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text_string)

def main(json_filename):
    # Illustrate basic use of built-in "pathlib" library
    json_path = Path(INPUT_FOLDER) / json_filename
    page_data = load_json(json_path)
    
    # Illustrate basic use of Jinja2 templates
    page_template = env.get_template("sample-webpage.html")
    page_html = page_template.render(**page_data)
    
    output_file_path = Path(OUTPUT_FOLDER) / json_filename
    output_file_path = output_file_path.with_suffix(".html")
    save_text_file(output_file_path, page_html)

if __name__ == "__main__":
    # Illustrate basic use of built-in "argparse" library
    # Command-line accepts a single argument, the filename of the input .json file
    parser = argparse.ArgumentParser()
    parser.add_argument("json_filename")
    args = parser.parse_args()
    
    main(args.json_filename)
