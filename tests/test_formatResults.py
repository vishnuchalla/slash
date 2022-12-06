"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: vamsitadikonda99@gmail.com

"""

import src.api.formatter as formatter
from bs4 import BeautifulSoup


def test_sortList():
    """
    Checks the sortList function
    """
    arr = [{"price": "$10"}, {"price": "$20"}, {"price": "$0"}]
    ansArr = [{"price": "$0"}, {"price": "$10"}, {"price": "$20"}]
    revAnsArr = [{"price": "$20"}, {"price": "$10"}, {"price": "$0"}]
    assert formatter.sortList(arr, "pr", False) == ansArr
    assert formatter.sortList(arr, "pr", True) == revAnsArr


def test_formatResults():
    """
    Checks the formatResults function
    """
    titles = [
        BeautifulSoup('<div class="someclass">title  </div>', "html.parser")
    ]
    prices = [
        BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")
    ]
    ratings = [
        BeautifulSoup(
            '<span class="w_EU">4.1 out of 5 Stars. 162 reviews</span>',
            "html.parser")
    ]
    links = []

    product = formatter.formatResult("example", titles, prices, links, ratings)
    ans = {
        "title": "title",
        "price": "$0.99",
        "website": "example",
        "rating": "4.1",
        "link": "https://www.ncsu.edu/"
    }
    print(product["website"], ans["website"])

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and \
           product["website"] == ans["website"] and product["rating"] == ans["rating"] \
           and product["link"] == ans["link"]
