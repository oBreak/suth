#!/bin/sh

cd ~/Projects/gh-suth/
info="Commit: $(date)"

echo "$info" >> timestamp.txt
echo "$info"
echo

# Push to repo

git add . # only required for first time
git commit -m "Commit comment"
git push
