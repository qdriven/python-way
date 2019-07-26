#!/usr/bin/env bash

echo "file name is $1"
echo "start to convert ......"
pandoc $1.md -o $1.html -c Github.css