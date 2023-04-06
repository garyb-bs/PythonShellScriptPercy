#!/bin/bash

var="$2"

echo "[LOG] Setting Percy Token"
set PERCY_TOKEN="$1"

echo "[LOG] Determining which command to run"

if [[ $var =~ "stop" ]];
then
  npx percy exec "$2"
  echo "[LOG] Successfully stopped Percy"
else
  npx percy exec -- "$2" "$3"
  echo "[LOG] Execution complete"
fi
