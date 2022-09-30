# MetricJoin Datasets

[![DOI](https://zenodo.org/badge/543141886.svg)](https://zenodo.org/badge/latestdoi/543141886)

This repository contains instructions to access the experimental data used in the paper "MetricJoin: Leveraging Metric Properties for Robust Exact Set Similarity Joins".

# Datasets

* For the datasets `AOL`, `BMS-POS`, `KOSARAK`, `NETFLIX`, and `ORKUT`, and the corresponding preprocessing instructions, we refer to [An Empirical Evaluation of Set Similarity Join Techniques - Compilation Instructions](http://ssjoin.dbresearch.uni-salzburg.at/datasets.html).
  Since `BMS-POS` and `NETFLIX` have small initial sizes, we scale them by a factor of 10 in our experiments using the technique described by Vernica et al. in "[Efficient parallel set-similarity joins using MapReduce](https://dl.acm.org/doi/10.1145/1807167.1807222)".
  The script to scale the datasets is located in `scripts/blowup.py`.
  After scaling a dataset, please consider re-preprocessing the dataset (the global token frequencies may have changed and duplicates may be introduced).

* `CELONIS` is a proprietary dataset provided by [Celonis SE](https://www.celonis.com/). 
   We are not allowed to publish it.

* The datasets `DBLP-V12`, `PUBCHEM`, and `TWITTER` are already preprocessed, i.e., the set elements are ordered by their inverse global token frequencies, the sets are sorted by their size, and duplicates have been removed.
  To download them, please run `sh scripts/download-data.sh`.
  Licensing information can be found in the respective `README.md` files.

