#!/bin/bash

set -eE -o pipefail

for dir in */; do
    cd $dir
    paru -U
    cd ..
done
