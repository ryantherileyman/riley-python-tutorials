import argparse
from pathlib import Path
from website_builder_utils import PRODUCT_INPUT_FOLDER, OUTPUT_FOLDER, env, load_json, save_text_file

def get_sku_id_list():
    # For demonstration purposes, just a flat array of SKU ID's
    # Would actually want to store these in a central location
    result = [ "1000", "1001", "1002" ]
    return result

def build_meta_description(product_data):
    result = f"View details for fake product #{product_data['sku_id']} - {product_data['name']}"
    return result

def build_product_page(sku_id):
    # Illustrate basic use of built-in "pathlib" library
    product_json_filename = "sku_" + sku_id + ".json"
    product_json_path = Path(PRODUCT_INPUT_FOLDER) / product_json_filename
    product_data = load_json(product_json_path)
    
    template_data = {
        "product_data": product_data,
        "meta_description": build_meta_description(product_data)
    }
    
    # Illustrate basic use of Jinja2 templates
    product_template = env.get_template("product_page.html")
    product_page_html = product_template.render(**template_data)
    
    product_html_filename = "products/sku_" + sku_id + ".html"
    product_html_path = Path(OUTPUT_FOLDER) / product_html_filename
    save_text_file(product_html_path, product_page_html)
    
    print(f"Built product page for SKU #{product_data['sku_id']}")

def build_all_product_pages():
    sku_id_list = get_sku_id_list()
    for curr_sku_id in sku_id_list:
        build_product_page(curr_sku_id)

def parse_args():
    # Illustrate basic use of built-in "argparse" library
    # Command-line accepts a single argument, either the SKU # or "--all" to build all product pages
    parser = argparse.ArgumentParser(description="Build product pages using Jinja2")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("sku_id", nargs="?", help="SKU of the product to build a page for")
    group.add_argument("--all", action="store_true", help="Build pages for all products")
    
    result = parser.parse_args()
    return result

def main():
    args = parse_args()
    
    if args.all:
        build_all_product_pages()
    
    elif args.sku_id:
        build_product_page(args.sku_id)
    
    else:
        print("Invalid arguments")
        sys.exit(1)

if __name__ == "__main__":
    main()
