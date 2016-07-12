# Description
This repository contains datasets for benchmarking the tasks of:
* (T1) identifying subject column of a table;
* (T2) matching Web Table columns to the properties inside knowledge bases (KBs), for instance, DBpedia;
* (T3) Open Table Extraction.

## [T2D Gold Standard for Matching Web Tables to DBpedia](http://webdatacommons.org/webtables/goldstandard.html)
T2D Gold Standard (T2D) consists of two parts:
* schema-level and
* entity-level gold standards.

To address the task of matching Web Table columns to the properties inside KBs, schema-level gold standard should be used. It contains 1,748 tables of which 762 can be mapped to DBpedia classes and 7983 columns which correspond to DBpedia properties.
Entity-level gold standard, which contains row-to-entity correspondences, does not serve the tasks defined above and thus is not included.
We analyze the gold standard, show that it contains more than XX% (TODO: calculate) erroneous annotations in [the T2D subfolder](./T2D/README.md).

## T2DStar Gold Standard
T2DStar was developed by the authors of this repository to address the problems of T2D.
In particular, the task of subject column identification can not be addressed by T2D as subject columns are not identified explicitly.
Also, we noticed incorrect/incomplete property annotations, while working with T2D.
To create T2DStar we curated a part of T2D, which was annotated by experts.
The description of the curation process as well as differences between T2D and T2DStar are further described in [the T2DStar subfolder](./T2DStar/README.md).
