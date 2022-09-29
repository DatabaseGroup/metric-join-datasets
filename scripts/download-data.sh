#!/bin/bash

echo "Download data"
mkdir -p data
cd data

git clone https://frosch.cosy.sbg.ac.at/datasets/sets/dblp-v12.git
git clone https://frosch.cosy.sbg.ac.at/datasets/sets/pubchem.git
git clone https://frosch.cosy.sbg.ac.at/datasets/sets/twitter.git

echo "Done"
