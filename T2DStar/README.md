# T2DStar Gold Standard for Matching Web Tables to DBpedia
T2DStar can be used to benchmark the tasks [T1](../README.md) and [T2](../README.md).

## Description
T2DStar is created to address the problems of [T2D](../T2D/README.md).
In T2DStar we addressed two problems separately.
First, we annotated randomly selected T2D tables with subject columns.
Then, we annotate properties for the tables.

To annotate subject columns we developed a special Web UI for the task. ![Subject Column Annotation Interface][subjectcolumnannotationinterface]
The interface gives a possibility to select 5 table types: normal (i.e. vertical listing), layout, vertical (i.e. horizontal listing), statistical and not English tables.
For the vertical listings experts users were asked to select subject column.

Using developed web UI we involved 15 expert users to annotate 322 randomly picked tables from T2D schema-level with 2 annotators per table.
We discarded the tables where the experts did not agree.
As a result, the 116 tables that (1) had no subject column at all (4 tables) and (2) which possessed a subject column upon which the experts agreed (112 tables) were included into T2DStar.
The F-measure achieved by the annotator as proposed in [1] is: F = (2 \* 116) / (2 \* 116 + (322 - 116)) = 0.53.
According to [2], the interval (0.41, 0.60) represents moderate agreement strength. This hints at how difficult the problem at hand really is.

To improve the quality of property annotation of T2D, we re-annotated the tables and involved 12 Semantic Web experts to perform the annotation task.
All experts were experienced DBpedia users or contributors.
Each user annotated 20 tables (2 annotations per table).
However, to reduce the time per annotation, we also displayed property suggestions from the LOV search engine.
On average, a user spent approximately 30 minutes to complete the task.
The interface developed for property annotations is shown below: ![Property Annotation Interface][propertyannotationinterface]

Out of 116 annotated tables, 90 (77.5%) tables had properties upon which the experts agreed.
Moreover, the experts agreed on 236 (53.5%) properties for the 441 columns we considered in T2DStar (subject columns excluded).
The F-measure for the property annotation task is defined as F = (2 \* 236)/(2 \* 236 + (441 - 236)) = 0.70.
According to [2] (0.61, 0.80) interval represents substantial agreement strength.

### Structure of the T2DStar Gold Standard
We organize T2DStar repository in the following way:
* tables/ folder contains original CSV tables,
* subject_column.csv file in the root directory contains subject column annotations and has the following structure:

| CSV file identifier | Subject Column ID |
|-------------------------------|

Subject Column ID starts with 0. For tables without subject columns the value is "-1".
* properties/ folder contains property annotations in CSV with the following structure:

| propertyUri | columnIndex | hasProperty |
|-------------------------------|

"propertyUri" is a property URI from DBpedia ontology or empty string. columnIndex starts from 0.
hasProperty indicates if column should be mapped to property, but DBpedia does not have this property (these annotations are included for the task [T3](../README.md)).

* properties_t2d_format/ folder contains property annotations in T2D format (i.e. does not contain annotations for the task [T3](../README.md)) with the following structure:

| DBpedia property URI | Column header (value from the first row) |	Is key column (boolean) |	Column index|
|-------------------------------|

### Citations

[1] Hripcsak, George, and Adam S. Rothschild. "Agreement, the f-measure, and reliability in information retrieval." Journal of the American Medical Informatics Association 12.3 (2005): 296-298.

[2] Landis, J. Richard, and Gary G. Koch. "The measurement of observer agreement for categorical data." biometrics (1977): 159-174.

[subjectcolumnannotationinterface]: https://dl.dropboxusercontent.com/u/4882345/t2dstargithub/imgs/help-sc.png "Subject Column Annotation Interface"
[propertyannotationinterface]: https://dl.dropboxusercontent.com/u/4882345/t2dstargithub/imgs/help.png "Property Annotation Interface"
