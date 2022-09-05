#!/bin/bash
# script that takes displays the size of the body of request to that URL
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
