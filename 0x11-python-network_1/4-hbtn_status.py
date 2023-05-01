# /usr/bin/python3
"""
Fetch https://alx-intranet.hbtn.io/status
using requests package
"""

import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
