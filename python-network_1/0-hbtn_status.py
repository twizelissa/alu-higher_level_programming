#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import urllib.request

url = 'https://intranet.hbtn.io/status'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    '\n    AppleWebKit/537.36 (KHTML, like Gecko)'
    '\n    Chrome/99.0.4844.84 Safari/537.36',
}
if __name__ == "__main__":
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
