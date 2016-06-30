# [T2D Gold Standard for Matching Web Tables to DBpedia](http://webdatacommons.org/webtables/goldstandard.html) 
We include T2D schema-level gold standard in this repository.
T2D can be used to benchmark the task [T2](../README.md).

## Description
For complete description of the standard please refer to [the official website](http://webdatacommons.org/webtables/goldstandard.html).
Here, we provide information on the structure, problems of T2D as well as code snippets for usage (in Python).

### Structure of the schema-level T2D
The schema-level T2D consists of:
* a tar archive with Web Tables (CSV files),
* a tar archive with a CSV file for each Web Table where property mappings are listed,
* and a CSV file with classes (line per table).

We organize the repository in the following way:
* original Web Tables are in tables_complete folder (1,748 CSV files),
* attributes_complete folder consists of files with property mappings for the Web Tables from tables_complete (777 CSV files)
* we keep classes_complete.csv in the root folder (1688 lines, i.e. for 1688 Web Tables).
Originally attributes_complete contained 1,748 files, however we delete files containing no property mappings.
Out of total 1,748 Web Tables 777 have property mappings.
All other (i.e. 971) considered as layout tables, which can not be mapped.

### Statistics of the schema-level T2D

### Code snippets for the usage
