#!/bin/bash
# Takes in a URL as an argument & displays body of response
curl -s "$1" -H "X-School-User-Id:98"
