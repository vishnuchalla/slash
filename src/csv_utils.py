"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

"""
The formatter module focuses on processing raw text and returning it in 
the required format. 
"""

import csv

def write_data(results):
    fieldnames = ['timestamp', 'title', 'price', 'website', 'rating']
    with open("items.csv", "w", encoding="UTF-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)