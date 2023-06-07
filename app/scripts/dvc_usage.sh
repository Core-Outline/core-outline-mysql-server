#!/bin/bash


commit = $@
git reset --hard @{commit}
git pull

dvc pull file.csv