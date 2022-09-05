#!/bin/bash
# Script that sents a header variable 'X-HolbertonSchool-User-Id' with the value '98'.
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
