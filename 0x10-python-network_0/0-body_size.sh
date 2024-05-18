#!/bin/bash
# Takes the URL sends a request to that url
curl -s "$1" | wc -c
