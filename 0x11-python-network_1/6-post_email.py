#!/usr/bin/python3
"""
Send POST request to URL with email parameter
Display the body of the response decoded in utf-8
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    req = requests.post(url, value)
    print(res.text)
