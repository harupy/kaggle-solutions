#!/usr/bin/env bash

ws_lines=""  # lines containing trailing whitespaces.
nl_files=""  # files that don't end with a newline.

for file in $(git ls-files | sed -e 's/^/.\//')
do
  lines=$(egrep -rnIH " +$" $file | cut -f-2 -d ":")
  if [ ! -z "$lines" ]; then
    ws_lines+=$([[ -z "$ws_lines" ]] && echo "$lines" || echo $'\n'"$lines")
  fi

  if [ ! -z "$(tail -c 1 $file)" ]; then
    nl_files+=$([[ -z "$nl_files" ]] && echo "$file" || echo $'\n'"$file")
  fi
done

exit_code=0

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
