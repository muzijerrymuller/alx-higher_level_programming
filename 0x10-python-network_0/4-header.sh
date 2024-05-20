#!/bin/bash
# Takes in a URL as an argument & displays body of response
curl "$1" -s -X GET -H "X-HolbertonSchool-User-Id:98"
