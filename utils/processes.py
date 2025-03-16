from selectolax.parser import Node
from datetime import datetime
import pandas as pd
import re

def get_attrs_from_nodes(n:Node, attr:str):
    if n is None or not issubclass(Node, type(n)):
        raise ValueError("sorry node is not type of selectolax node")
    return n.attributes.get(attr)

def get_n_list(input_list: list, n: int):
    return input_list[:n]

def reformat_date(date_raw:str, input_format:str='%b %d, %Y', output_format:str='%Y-%m-%d'):
    dt_object=datetime.strptime(date_raw, input_format)
    return datetime.strftime(dt_object, output_format)

def get_currency(price:str):
    return 

def regex(pattern:str, raw: str):
    return re.findall(pattern, raw)[0]

def format_and_transform(attrs: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_nodes(n, "src"),
        "tags": lambda input_list: get_n_list(input_list, 5),
        "release_date": lambda date: reformat_date(date, '%b %d, %Y', '%Y-%m-%d'),
        "price_currency": lambda raw: regex(r'[^\d\.\,]+', raw),
        "sales_price": lambda raw: float(regex(r'[\d\.\,]+', raw).replace(",",".")),
        "original_price": lambda raw: float(regex(r'[\d\.\,]+', raw).replace(",","."))
    }
    for k, v in transforms.items():
        if k in attrs:
            attrs[k]=v(attrs[k])
    return attrs

def save_file_to(filename:str="extract", data:list[dict]=None):
    if data is None:
        raise ValueError("a data of type list of dictionaries must be provided")
    df=pd.DataFrame(data)
    filename=f"{datetime.now().strftime("%Y_%m_%d")}-{filename}.csv"
    df.to_csv(filename, index=False)