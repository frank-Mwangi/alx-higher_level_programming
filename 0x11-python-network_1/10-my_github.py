#!/usr/bin/python3
"""
takes Github credentials as arguments and
Displays your id
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(url, auth=(username, password))
    print(res.json().get('id'))
