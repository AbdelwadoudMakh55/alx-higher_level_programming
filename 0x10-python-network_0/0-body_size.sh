#!/usr/bin/env bash
# Sending a request and displaying the body size
curl -sI "$1" | grep "content-length" | cut -c 17-
