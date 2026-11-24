#!/bin/bash
# Sends a GET request to a URL, following redirects, and displays the body only for a 200 response
curl -sLf "$1"
