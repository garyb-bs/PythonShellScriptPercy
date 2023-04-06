#!/bin/sh
# First Argument: Percy Token
# Second Argument: Python
# Third Argument: File Name
# Fourth Argument: Function Name
# Fifth Argument: Unique ID for PERCY_PARALLEL_NONCE
echo "$#"

echo "[LOG] Setting Percy Token"

export PERCY_TOKEN="$1"
export PERCY_PARALLEL_TOTAL="5"
export PERCY_PARALLEL_NONCE="$5"

echo "[LOG] Set PERCY_PARALLEL_NONCE to $4"
echo "[LOG] Set PERCY_PARALLEL_TOTAL to 5"


echo "[LOG] Determining which command to run"

npx percy exec --parallel -- "$2" "$3" "$4" "$5"

echo "[LOG] Execution complete"
