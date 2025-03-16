from selectolax.parser import HTMLParser
from utils.extract import extract_html_from
from config.tools import get_config
from utils.parse import parse_raw_attribute
from utils.processes import format_and_transform, save_file_to
timeout=90000
if __name__ == "__main__":
    config=get_config()
    html=extract_html_from(url=config.get("url"), 
                           wait_for=config.get("container").get("selector"))   
    tree=HTMLParser(html)
    nodes=tree.css(config.get("container").get("selector"))
    game_data=[]
    for n in nodes:
        attrs=parse_raw_attribute(n, config.get("items"))
        attrs=format_and_transform(attrs)
        game_data.append(attrs)
    save_file_to("extract",game_data)
