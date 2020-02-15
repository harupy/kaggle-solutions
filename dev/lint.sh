#!/usr/bin/env bash

# This script detects the following violations for all tracked files:
# - trailing whitespaces
# - no new line at EOF

ws_lines=""  # lines containing trailing whitespaces.
nl_files=""  # files that don't end with a newline.

# Iterate over all tracked files.
for file in $(git diff --name-only origin/master | sed -e 's/^/.\//')
do
  # trailing whitespaces
  lines=$(egrep -rnIH " +$" $file | cut -f-2 -d ":")
  if [ ! -z "$lines" ]; then
    ws_lines+=$([[ -z "$ws_lines" ]] && echo "$lines" || echo $'\n'"$lines")
  fi

  # no new line at EOF
  if [ ! -z "$(tail -c 1 $file)" ]; then
    nl_files+=$([[ -z "$nl_files" ]] && echo "$file" || echo $'\n'"$file")
  fi
done

exit_code=0

# If violations detected, change the exit code to 1 to make the CI fail.
if [ ! -z "$ws_lines" ]; then
  printf "\n%s\n" "# Trailing whitespace"
  printf "%s\n" "${ws_lines[@]}"
  exit_code=1
fi

if [ ! -z "$nl_files" ]; then
  printf "\n%s\n" "# No newline at end of file"
  printf "%s\n" "${nl_files[@]}"
  exit_code=1
fi

exit $exit_code
