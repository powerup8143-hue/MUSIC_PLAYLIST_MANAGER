#!/usr/bin/env bash
set -e
echo "Compiling playlist.c..."
gcc -O2 playlist.c -o playlist
echo "Compiled -> ./playlist"
