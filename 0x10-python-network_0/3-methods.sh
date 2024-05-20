#!/bin/bash
# Displays a bash script
curl -sI ALLOW "$1" -L | grep "Allow"  | cut -d " " -f2-
