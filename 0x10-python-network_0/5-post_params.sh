#!/bin/bash
# Script that displays the body of the response with some variables.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
