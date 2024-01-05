#!/bin/bash
# Sending a POST request with parameters
curl -v -X POST -d "{"email": "test@gmail.com", "subject":  "will always be here for PLD"}"  "$1" -s
