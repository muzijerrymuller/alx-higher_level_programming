#!/bin/bash
# Takes in a URL as an argument & displays body of response
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
