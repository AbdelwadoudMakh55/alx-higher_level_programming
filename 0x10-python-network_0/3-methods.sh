#!/bin/bash
# Sending an OPTIONS request
curl -sI "$1" | grep "Allow" | cut -c 8-
