#!/bin/bash

git add .
git commit -m "Latest data changes"
git push
dvc add data.zip
dvc push data.zip

echo git log -1 | sed -n '1s/commit //p'
