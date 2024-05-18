#!/bin/bash
# Takes url sends a GET request to it and displays the body.
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
