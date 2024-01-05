#!/bin/bash
# Displaying status code
curl -sI "$1" | grep "HTTP/1.1" | cut -c 10-
