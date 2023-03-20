#!/bin/bash
echo "Starting Percy Server"
set PERCY_TOKEN="$1"
percy exec "$2"
