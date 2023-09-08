import requests

from bs4 import BeautifulSoup


def get_html():
    url = "https://zimpricecheck.com/price-updates/official-and-black-market-exchange-rates/"
    request_data = requests.get(url)

    if request_data.status_code == 200:
        raw_html = BeautifulSoup(request_data.content, "html.parser")
        cleaned_html = raw_html.find("figure", class_="wp-block-table")
        html_table = cleaned_html.find_all("tr")
        html_table.pop(0)
        return html_table
    else:
        return None

def rates_list():
    html_list = get_html()
    rate_list = [ ((x.text).strip()).splitlines() for x in html_list if html_list is not None ]
    rate_dict = {rate_list_item[0]:rate_list_item[1] for rate_list_item in rate_list}
    return rate_dict







