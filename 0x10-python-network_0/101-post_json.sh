#!/bin/bash
# Sending a POST request with parameters JSON
curl -X POST "$1" -d @"$2" -s
