#!/usr/bin/python3
"""
Send POST request to URL with email parameter
Display the body of the response decoded in utf-8
"""

import sys
from urllib import parse, request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
