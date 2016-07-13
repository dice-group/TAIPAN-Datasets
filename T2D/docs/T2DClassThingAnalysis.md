# Analysis of T2D table with class annotations owl:Thing

## Identified problems
All of the owl:Thing tables have missing property annotations. We were Identified those missing property annotations as annotation mistakes (see examples below).

* Tables without any property annotations, not containing subject column are identified as owl:Thing.
  * [Example table](./T2DClassThing/13454929_38_5704125866480389014.csv.md)
* Tables about particular classes are annotated as owl:Thing (missing property annotations).
  * [dbr:Stock_exchange](./T2DClassThing/17167790_0_5345921575574015166.csv.md) annotated as owl:Thing
  * [dbo:Plant](./T2DClassThing/36947132_3_6827197521362373979.csv.md)
  * [dbo:Plant](./T2DClassThing/38987686_0_7135762360717955737.csv.md)
  * [dbo:Hospital](./T2DClassThing/46501732_0_7847615138468645815.csv.md)
  * [Backgammon game](./T2DClassThing/61371918_137_4508398029601236682.csv.md)
  * [Another table about backgammon game](./T2DClassThing/76431189_9_8247267217236095245.csv.md)
  * [dbo:Country](./T2DClassThing/62662505_0_866780568064211104.csv.md)
  * [Camping sides](./T2DClassThing/76901387_5_7208130730915207843.csv.md)
  * [Weather reports](./T2DClassThing/89472016_0_7556326221906081768.csv.md)
  * [Product reviews](./T2DClassThing/94145647_0_4411495338698364870.csv.md)
* Tables with broken encoding/or in different from English languages are annotated as owl:Thing
  * [Example table](./T2DClassThing/44942480_0_2396126158991576450.csv.md)
  * [Example table](./T2DClassThing/52425262_0_5182099736652132739.csv.md)
* Layout tables are annotated as owl:Thing
  * [Example table](./T2DClassThing/67179268_0_2295221666082539065.csv.md)
* There are tables containing property annotations with mistakes as well
  * ["size: adjustable" is identified as dbo:fileSize](./T2DClassThing/83626253_0_1722513863780895644.csv.md)

## List of involved CSV files
As number of involved CSV tables is too large (978), we do not include it in this document. To get the full list please use the following shell command
```
cat classes_complete.csv | grep Thing
```
