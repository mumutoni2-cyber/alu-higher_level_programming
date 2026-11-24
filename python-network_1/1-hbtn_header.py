#!/usr/bin/python3
"""Displays the X-Request-Id header value of the response from a URL."""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))
