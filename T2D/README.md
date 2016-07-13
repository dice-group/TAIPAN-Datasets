# [T2D Gold Standard for Matching Web Tables to DBpedia](http://webdatacommons.org/webtables/goldstandard.html)
T2D can be used to benchmark the task [T2](../README.md).
Additionally, T2D can be extended to benchmark the task [T1](../README.md), however as this task was not addressed explicitly by the authors of the dataset, we encourage to use T2DStar for [T1](../README.md).

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

### Problems of the schema-level T2D
* Property mapping files in the attributes_complete folder contained ^M character, which recognized as newline character on unix systems (23 CSV files) [Fixed]
* The same applies for the Web Tables (172 CSV files) [Fixed]
* The class annotations ("classes_complete.csv") IDs differ from tables_complete/attributes_complete IDs (extension .tar.gz instead of .csv)
* Contain files with multiple rdfs:label (i.e. subject columns). It is advisable to blacklist these files, when working with T2D ([see discussion here](./docs/MultipleSubjectColumns.md))
  * 10453276_0_7370421113682439765.csv
  * 17769450_0_8003688464359007517.csv
  * 24003697_0_8569423605161973748.csv
  * 27100349_0_4569354779422013472.csv
  * 2849108_0_5238405355789704342.csv
  * 34501970_0_2477755352098394078.csv
  * 37402655_0_9176587382722029523.csv
  * 38146710_0_3777366193503047044.csv
  * 42846393_2_6922315287291245126.csv
  * 47101798_1_4424372688353800689.csv
  * 48495038_0_1033305650426317920.csv
  * 53264869_1_530811839053269226.csv
  * 54802079_0_6709615660980454909.csv
  * 60884685_1_5420701306478974044.csv
  * 61108455_0_4273649346480472385.csv
  * 63198107_0_5688435789215389159.csv
  * 78616821_0_2458612333287914096.csv
  * 80992694_0_3506971500806631353.csv
  * 83577589_0_3008022348570648346.csv
* T2D annotates 978 tables with owl:Thing class. We analyze the annotations of randomly selected 15 tables [here](./docs/T2DClassThingAnalysis.md) 
* We further analyze randomly selected tables from T2D, which were re-annotated during creation of [T2DStar](../T2DStar/README.md). The analysis is described [here](./docs/T2DTableAnalysis.md).

### Code snippets for the usage
* (extract_subject_column)[./snippets/extract_subject_column.py] snippet iterates over all annotated CSV tables and extracts subject columns into a separate file. Missing subject column is indicated with "-1"
