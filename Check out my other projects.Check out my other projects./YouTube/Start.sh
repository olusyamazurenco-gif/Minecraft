#!/bin/sh
echo "🚀 Launching MyTube Clone..."
echo "Checking Python3..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install Python3 first."
    exit
fi
echo "Starting server..."
python3 server.py
