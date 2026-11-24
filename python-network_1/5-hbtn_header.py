#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response from a URL."""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
