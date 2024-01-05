#!/bin/bash
# Sending a POST request with parameters JSON
curl -d @"$2" "$1" -s
