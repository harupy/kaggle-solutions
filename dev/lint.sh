#!/usr/bin/env bash

# The line below finds lines containing traling white spaces.
# -n: Prefix each line of output with the line number.
# -I: Process a binary file as if it did not contain matching data.
lines=$(git ls-tree -r HEAD --name-only | xargs egrep -nI " +$" | cut -f 1,2 -d :)

if [ ! -z "$lines" ]; then
  printf "%s\n" "${lines[@]}"
  printf "\n%s\n" "Found trailing whitespaces."
  exit 1 
fi 

pipenv run flake8 tools tests
