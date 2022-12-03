"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: vamsitadikonda@gmail.com

The scraper module holds functions that actually scrape the e-commerce websites
"""

import requests
import formatter
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser


def httpsGet(URL):
    """
    The httpsGet function makes HTTP called to the requested URL with custom headers
    return: scraped html content from the URL
    """
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }
    page = requests.get(URL, headers=headers)
    return page.content


def httpsGetTarget(URL, query):
    """
    The httpsGetTarget function makes HTTP called to the requested URL with custom headers and params specific to Target website
    return: returns json from the target URL
    """
    headers = {
        'authority':
            'redsky.target.com',
        'accept':
            'application/json',
        'accept-language':
            'en-US,en;q=0.9,mr;q=0.8',
        'origin':
            'https://www.target.com',
        'referer':
            URL,
        'sec-ch-ua':
            '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile':
            '?0',
        'sec-ch-ua-platform':
            '"Windows"',
        'sec-fetch-dest':
            'empty',
        'sec-fetch-mode':
            'cors',
        'sec-fetch-site':
            'same-site',
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    params = {
        'key': 'ff457966e64d5e877fdbad070f276d18ecec4a01',
        'channel': 'WEB',
        'count': '24',
        'default_purchasability_filter': 'true',
        'include_sponsored': 'true',
        'keyword': query,
        'offset': '0',
        'page': f'/s/{query}',
        'platform': 'desktop',
        'pricing_store_id': '961',
        'scheduled_delivery_store_id': '961',
        'store_ids': '961,2721,1932,2785,3255',
        'useragent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'visitor_id': '018366FA85BE0201AE0C2E6660BAB7D2',
        'zip': '27606',
    }

    response = requests.get(
        'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
        params=params,
        headers=headers)
    results_json = response.json()
    return results_json


def searchAmazon(query, linkFlag, product_queue, limit=3):
    """
    The searchAmazon function scrapes amazon.com
    :param query: search keyword to perform the query
    return: returns the products list from amazon
    """
    query = formatter.formatSearchQuery(query)
    URL = f'https://www.amazon.com/s?k={query}'
    page = httpsGet(URL)
    tree = HTMLParser(page)
    cnt = 0
    for node in tree.tags("div"):
        if 'data-component-type' in node.attributes and node.attributes['data-component-type'] == "s-search-result":
            title = node.css_first("h2 a span").text()
            price = node.css_first("span.a-price span").text()
            link = node.css_first("h2 a.a-link-normal").text()
            rating = node.css_first("span.a-icon-alt").text()
            product = formatter.formatResult1("amazon", title, price, link, rating)
            if not linkFlag:
                del product["link"]
            if price is not None:
                product_queue.put(product)
            cnt += 1
            if cnt == limit:
                break


def searchWalmart(query, linkFlag, product_queue, limit=3):
    """
    The searchWalmart function scrapes walmart.com
    :param query: search keyword to perform the query
    return: returns the product list from walmart
    """
    query = formatter.formatSearchQuery(query)
    URL = f'https://www.walmart.com/search?q={query}'
    page = httpsGet(URL)
    tree = HTMLParser(page)
    cnt = 0
    for node in tree.tags("div"):
        if 'data-item-id' in node.attributes:
            title = node.css_first("span.lh-title").text() if node.css_first("span.lh-title") else None
            price = node.css_first("div.lh-copy").text() if node.css_first("div.lh-copy") else None
            link = node.css_first("a").attributes["href"] if node.css_first("a") else None
            rating = node.css_first("span.w_EU").text() if node.css_first("span.w_EU") else None
            product = formatter.formatResult1("walmart", title, price, link, rating)
            if not linkFlag:
                del product["link"]
            if price is not None:
                product_queue.put(product)
            cnt += 1
            if cnt == limit:
                break


def searchTarget(query, linkFlag, product_queue, limit=3):
    """
    The searchTarget function scrapes hidden API of target.com
    :param query: search keyword to perform the query
    return: returns the product list from target
    """
    query = formatter.formatSearchQuery(query)
    URL = f'https://www.target.com/s?searchTerm={query}'
    page = httpsGetTarget(URL, query)
    results = page['data']['search']['products']
    products = []
    cnt=0
    for idx in range(len(results)):
        titles = results[idx]['item']['product_description']['title'].replace(
            '&#8482;', '')
        prices = results[idx]['price']['formatted_current_price']
        if ('parent' in results[idx].keys()):
            ratings = results[idx]['parent']['ratings_and_reviews'][
                'statistics']['rating']['average']
        else:
            ratings = results[idx]['ratings_and_reviews']['statistics'][
                'rating']['average']
        if 'primary_brand' in results[idx]['item']:
            links = URL + str(
                results[idx]['item']['primary_brand']['canonical_url'])
        else:
            links = ''
        product = formatter.formatResult("target", titles, prices, links,
                                         ratings)
        if not linkFlag:
            del product["link"]
        if prices is not None:
            product_queue.put(product)
        cnt += 1
        if cnt == limit:
            break
