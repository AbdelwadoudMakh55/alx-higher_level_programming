#!/bin/bash
# Sending a request and displaying the body size
curl -sI "$1" | grep "Content-Length" | cut -c 17-
