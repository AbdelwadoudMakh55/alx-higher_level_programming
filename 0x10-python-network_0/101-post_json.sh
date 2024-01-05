#!/bin/bash
# Sending a POST request with parameters JSON
curl -X POST -H 'Content-Type: application/json' -d @"$2" "$1" -s
