#!/usr/bin/python3
"""
Takes in URL, sends request to it and displays
the value of the X-Request-Id header variable
"""

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as res:
        print(dict(res.headers).get("X-Request-Id"))
