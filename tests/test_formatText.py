"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: vamsitadikonda99@gmail.com

"""

import src.api.formatter as formatter


def test_formatSearchQuery():
    """
    Checks the formatSearchQuery function
    """
    assert formatter.formatSearchQuery("1 2") == "1+2"
    assert formatter.formatSearchQuery("A B") == "A+B"
    assert formatter.formatSearchQuery("ABC") == "ABC"


def test_formatTitle():
    """
    Checks the formatTitle function
    """
    assert formatter.formatTitle("0" * 50) == "0" * 40 + "..."
    assert formatter.formatTitle("0" * 5) == "0" * 5
