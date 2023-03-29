#!/bin/sh
echo "$#"

var="$2"

echo "[LOG] Setting Percy Token"

export PERCY_TOKEN="$1"
export PERCY_PARALLEL_TOTAL="5"
export PERCY_PARALLEL_NONCE="$4"

echo "[LOG] Set PERCY_PARALLEL_NONCE to $4"
echo "[LOG] Set PERCY_PARALLEL_TOTAL to 5"


echo "[LOG] Determining which command to run"

if [[ $var =~ "stop" ]];
then
  npx percy exec stop
  echo "[LOG] Successfully stopped Percy"
else
  npx percy exec --parallel -- "$2" "$3"
  echo "[LOG] Execution complete"
fi
