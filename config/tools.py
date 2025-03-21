import json

_config={
    "url": "https://store.steampowered.com/specials",
    "meta": {
        "name": "steam sales scraper",
        "description": "Extracts the game info and current price from steam",
        "version": "0.1"
    },
    "container": {
        "name": "stores_sales_div",
        "selector": "div[class*='gASJ2lL']",
        "match": "all",
        "type": "node"
    },
    "items": [
        {
            "name": "title",
            "selector": "div[class*='StoreSaleWidgetTitle']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "thumbnail",
            "selector": "div[class*='CapsuleImageCtn'] > img",
            "match": "first",
            "type": "node"
        },
        {
            "name": "tags",
            "selector": "div[class='_2bkP-3b7dvr0a_qPdZEfHY'] > a",
            "match": "all",
            "type": "text"
        },
        {
            "name": "release_date",
            "selector": "div[class='_1qvTFgmehUzbdYM9cw0eS7']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "price_currency",
            "selector": "div[class*='_3j4dI1yA7cRfCvK8h406OB']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "sales_price",
            "selector": "div[class*='_3j4dI1yA7cRfCvK8h406OB']",
            "match": "first",
            "type": "text"
        },
        {
            "name": "original_price",
            "selector": "div[class*='_3fFFsvII7Y2KXNLDk_krOW']", 
            "match": "first",
            "type": "text"
        },
        {
            "name": "discount_percentage",
            "selector": "div[class*='cnkoFkzVCby40gJ0jGGS4']",
            "match": "first",
            "type": "text"
        }
    ]
}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)
    return _config


def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)

if __name__=="__main__":
    generate_config()
