from pathlib import Path
from build_product_page import get_sku_id_list
from website_builder_utils import PRODUCT_INPUT_FOLDER, OUTPUT_FOLDER, env, load_json, save_text_file

def build_home_page():
    sku_id_list = get_sku_id_list()
    
    template_data = {
        "sku_id_list": sku_id_list
    }
    
    home_template = env.get_template("home_page.html")
    home_page_html = home_template.render(**template_data)
    
    home_html_path = Path(OUTPUT_FOLDER) / "index.html"
    save_text_file(home_html_path, home_page_html)
    
    print("Built home page")

def main():
    build_home_page()

if __name__ == "__main__":
    main()
