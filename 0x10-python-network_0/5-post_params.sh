#!/bin/bash
# Sending a POST request with parameters
curl -X POST "$1" -H "Content-Type: application/json" -d "{"email": "test@gmail.com", "subject":  "will always be here for PLD"}" -s
