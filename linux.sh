#!/bin/sh
echo "Starting Percy Server"
export PERCY_TOKEN="$1"
percy exec "$2"
