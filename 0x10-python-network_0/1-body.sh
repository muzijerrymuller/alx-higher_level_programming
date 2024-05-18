#!/bin/bash
# Takes url sends a GET request to it and displays the body.
curl -sX GET "$1" -L
