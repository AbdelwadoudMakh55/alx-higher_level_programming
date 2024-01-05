#!/bin/bash
# Sending a GET request with a header variable
curl -s "$1" -H "X-School-User-Id: 98"
