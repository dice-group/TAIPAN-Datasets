# Multiple Subject Columns Problem

## List of involved CSV files

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

## Analysis of the Problem

Hypothetically, a table can have several rdfs:label columns (i.e. subject columns).
For instance, it can lists the name of the subject matter in different languages.
In this document, we analyze the tables with several subject columns from T2D gold standard and show that in most cases several rdfs:label annotations (i.e. subject columns) are attributed to an annotation mistake.
We proceed as follows:
* For each table we first show the table data.
* We also show property annotations. According to T2D the property annotations have the following header.

| DBpedia property URI | Column header (value from the first row) |	Is key column (boolean) |	Column index|
|-------------------------------|
* We show the class annotation for the table for the sake of completeness.
* We provide an example of RDF, which can be generated from T2D annotation.
* We provide a comment on the performed property annotation.

### 10453276_0_7370421113682439765.csv

#### Table Data

| "Keyword"       | "Avg Price" | "Price/Sf" |
|-----------------|-------------|------------|
| "Single Story"  | "$185483"   | "$133"     |
| "Two Story"     | "$293004"   | "$115"     |
| "Mountain View" | "$257720"   | "$121"     |
| "Price Reduced" | "$222994"   | "$122"     |
| "Cul De Sac"    | "$251615"   | "$124"     |
| "Pool"          | "$313494"   | "$109"     |
| "New Listings"  | "$221393"   | "$116"     |
| "Foreclosure"   | "$209135"   | "$113"     |
| "Short Sale"    | "$205858"   | "$111"     |
| "Loft"          | "$301613"   | "$112"     |
| "Custom Built"  | "$241064"   | "$122"     |
| "Tlc"           | "$161545"   | "$117"     |
| "City View"     | "$350682"   | "$119"     |
| "Golf Course"   | "$297937"   | "$116"     |
| "Gated"         | "$729159"   | "$105"     |

#### Property Annotations
|                                             |             |        |     |
|----------------------------------------------|-------------|--------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "Avg Price" | "True" | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Price/Sf"  | "True" | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Keyword"   | "True" | "0" |

#### Class Annotation

No class specified

#### T2D Based RDF
```
<http://example.com/10453276_0_7370421113682439765.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Single Story" .
<http://example.com/10453276_0_7370421113682439765.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "$185483" .
<http://example.com/10453276_0_7370421113682439765.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "$133" .
```

#### Comments

The table describes prices for real estate based on keywords.
The subject is a real estate, which has keyword(-s), average price, and price per square foot.
We argue, that this table does not contain subject column.
The original mapping has 3 "rdfs:label" properties for each of the columns.

### 17769450_0_8003688464359007517.csv

#### Table Data

| "&nbsp;" | "name"                                           | "artist"         | "time" | "price" | "&nbsp;"         |
|----------|--------------------------------------------------|------------------|--------|---------|------------------|
| "1"      | "daydreaming (luv it mix)"                       | "massive attack" | "5:27" | "$1.29" | "view in itunes" |
| "2"      | "daydreaming (brixton bass mix)"                 | "massive attack" | "5:22" | "$1.29" | "view in itunes" |
| "3"      | "daydreaming (luv it dub)"                       | "massive attack" | "5:26" | "$1.29" | "view in itunes" |
| "4"      | "unfinished sympathy (nellee hooper 12'' mix)"   | "massive attack" | "5:51" | "$1.29" | "view in itunes" |
| "5"      | "unfinished sympathy (perfecto mix)"             | "massive attack" | "5:18" | "$1.29" | "view in itunes" |
| "6"      | "safe from harm (perfecto mix)"                  | "massive attack" | "8:14" | "$1.29" | "view in itunes" |
| "7"      | "safe from harm (just a groove dub)"             | "massive attack" | "3:18" | "$1.29" | "view in itunes" |
| "8"      | "safe from harm (just a dub)"                    | "massive attack" | "3:13" | "$1.29" | "view in itunes" |
| "9"      | "hymn of the big wheel (nellee hooper mix)"      | "massive attack" | "5:52" | "$1.29" | "view in itunes" |
| "10"     | "be thankful for what you've got (perfecto mix)" | "massive attack" | "6:17" | "$1.29" | "view in itunes" |
| "11"     | "any love (larry heard mix)"                     | "massive attack" | "4:27" | "$1.29" | "view in itunes" |

#### Property Annotations
|                                              |          |         |     |
|----------------------------------------------|----------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "name"   | "True"  | "1" |
| "http://dbpedia.org/ontology/duration"       | "time"   | "False" | "3" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "artist" | "True"  | "2" |

#### Class Annotation

"17769450_0_8003688464359007517.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/17769450_0_8003688464359007517.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/17769450_0_8003688464359007517.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "daydreaming (luv it mix)" .
<http://example.com/17769450_0_8003688464359007517.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "massive attack" .
<http://example.com/17769450_0_8003688464359007517.csv/1> <http://dbpedia.org/ontology/duration> "5:27" .
```

#### Comments
The table lists the songs from an album of an artist in an online shop.
The data can be modeled as RDF in two different ways, depending on a use case at the hand:
* "artist" is a subject column (rdfs:label), "artist" released a song ("name") with duration "time", "price" and track number "" (i.e. first column).
* "name" is a subject column (rdfs:label), which was released by an "artist", has "time", "price" and track number ""
* There is no subject column (i.e. album is a subject). Then every row has a track "name", with track number "" (first row), written by "artist", with duration "time" and "price".

Originally, T2D lists two rdfs:labels "name" and "artist", which means that subject is identified by both artist and song name. That would mean that any row is linked to two URIs at the same time.

### 24003697_0_8569423605161973748.csv

#### Table Data

|     |                                 |                             |
|-----|---------------------------------|-----------------------------|
| "2" | "snow partridge"                | "lerwa lerwa"               |
| "2" | "tibetan snowcock"              | "tetraogallus tibetanus"    |
| "3" | "chestnut-throated partridge"   | "tetraophasis obscurus"     |
| "3" | "tibetan partridge"             | "perdix hodgsoniae"         |
| "2" | "chinese bamboo partridge"      | "bambusicola thoracica"     |
| "2" | "blood pheasant"                | "ithaginis cruentus"        |
| "2" | "temminck's tragopan"           | "tragopan temminckii"       |
| "2" | "koklass pheasant�������������" | "pucrasia macrolopha"       |
| "3" | "chinese monal"                 | "lophophorus lhuysii"       |
| "2" | "white eared pheasant"          | "crossoptilon crossoptilon" |

#### Property Annotations

|                                              |                  |        |     |
|----------------------------------------------|------------------|--------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "lerwa lerwa"    | "True" | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "snow partridge" | "True" | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "2"              | "True" | "0" |

#### Class Annotation

"24003697_0_8569423605161973748.tar.gz","Bird","http://dbpedia.org/ontology/Bird",""

#### T2D Based RDF
```
<http://example.com/24003697_0_8569423605161973748.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Bird> .
<http://example.com/24003697_0_8569423605161973748.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "2" .
<http://example.com/24003697_0_8569423605161973748.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "snow partridge" .
<http://example.com/24003697_0_8569423605161973748.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "lerwa lerwa" .
```

#### Comments

The table lists species of birds with their English and scientific (i.e. Latin) names.
The RDF can be modeled by selecting second column as a subject column.
Then for each row, the third column will represent [scientific name](http://dbpedia.org/ontology/scientificName).
The first column can not be guessed by human as it contains numerical information.

T2D defines all three columns as rdfs:label. While English and scientific names can be used as rdfs:labels (although more specific property for scientific name exists), it is incorrect to use it for numerical value in the first column

### 27100349_0_4569354779422013472.csv

#### Table Data

|                    |                                   |                                          |                     |           |
|--------------------|-----------------------------------|------------------------------------------|---------------------|-----------|
| "5 Jul 201221:15"  | "The Gipsy Kings&nbsp;"           | "Arena CivicaMilan"                      | "From&pound;40.6"   | "COMPARE" |
| "8 Jul 201218:00"  | "Kew the Music Gipsy Kings&nbsp;" | "Kew GardensLondon"                      | "From&pound;35.5"   | "COMPARE" |
| "8 Aug 201220:00"  | "The Gipsy Kings&nbsp;"           | "Wolf TrapWolf Trap"                     | "From&pound;60.85"  | "COMPARE" |
| "10 Aug 201220:00" | "The Gipsy Kings&nbsp;"           | "Humphreys Concerts By the BaySan Diego" | "From&pound;103.8"  | "COMPARE" |
| "15 Aug 201219:30" | "The Gipsy Kings&nbsp;"           | "Mountain WinerySaratoga"                | "From&pound;95.88"  | "COMPARE" |
| "18 Aug 201220:00" | "The Gipsy Kings&nbsp;"           | "Nokia Theatre Live - LaLos Angeles"     | "From&pound;139.99" | "COMPARE" |

#### Property Annotations

|                                              |          |         |     |
|----------------------------------------------|----------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "Title"  | "True"  | "1" |
| "http://dbpedia.org/ontology/cost"           | "cost"   | "False" | "3" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Artist" | "True"  | "2" |


#### Class Annotation

"27100349_0_4569354779422013472.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork",""

#### T2D Based RDF
```
<http://example.com/27100349_0_4569354779422013472.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/27100349_0_4569354779422013472.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "The Gipsy Kings" .
<http://example.com/27100349_0_4569354779422013472.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Arena CivicaMilan" .
<http://example.com/27100349_0_4569354779422013472.csv/1> <http://dbpedia.org/ontology/cost> "From £40.6" .
```

#### Comments

The table lists the ticket prices for the concerts at different locations.
The class annotation is incorrect and should be Event or Musical Event (gig, concert).
The data can be modeled as RDF as follows:
* There is no subject column (i.e. concert is a subject matter). Then every row has a concert "date/time" (first column), band name (second column), concert place (third column), the cheapest ticket price (fourth column).

Originally, T2D lists two rdfs:labels "Title" and "Artist", however the table talks about concerts, not songs in this case.

### 2849108_0_5238405355789704342.csv

#### Table Data

| "General Information" | ""                       | ""       |
|-----------------------|--------------------------|----------|
| "City Name"           | "Speed"                  | "&nbsp;" |
| "State"               | "North Carolina"         | "&nbsp;" |
| "Population 2000"     | "70"                     | "&nbsp;" |
| "Housing Units"       | "60"                     | "&nbsp;" |
| "Total Area"          | "square miles"           | "&nbsp;" |
| "Water Area"          | "square miles"           | "&nbsp;" |
| "Land Area"           | "square miles"           | "&nbsp;" |
| "Population Density"  | "247 people/square mile" | "&nbsp;" |
| "Housing Density"     | "212 units/square mile"  | "&nbsp;" |

#### Annotations

|                                                                |                      |         |     |
|----------------------------------------------------------------|----------------------|---------|-----|
| "http://dbpedia.org/ontology/PopulatedPlace/populationDensity" | "Population Density" | "False" | "8" |
| "http://www.w3.org/2000/01/rdf-schema#label"                   | "State"              | "True"  | "2" |
| "http://dbpedia.org/ontology/populationAsOf"                   | "Population 2000"    | "False" | "3" |
| "http://www.w3.org/2000/01/rdf-schema#label"                   | "City Name"          | "True"  | "1" |

#### Class Annotation

"2849108_0_5238405355789704342.tar.gz","City","http://dbpedia.org/ontology/City","0"

#### T2D Based RDF
```
<http://example.com/2849108_0_5238405355789704342.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/City> .
<http://example.com/2849108_0_5238405355789704342.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "&nbsp;".
<http://example.com/2849108_0_5238405355789704342.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Speed".
<http://example.com/2849108_0_5238405355789704342.csv/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/City> .
<http://example.com/2849108_0_5238405355789704342.csv/2> <http://www.w3.org/2000/01/rdf-schema#label> "&nbsp;".
<http://example.com/2849108_0_5238405355789704342.csv/2> <http://www.w3.org/2000/01/rdf-schema#label> "North Carolina".
```

#### Comments

According to [1] such tables should be classified as horizontal listings.
Identifying the row containing the subjects and predicates pose the biggest extraction challenge from this table type.
The header of a table is in the first column.
Before annotation and transformation to RDF such a table has to be rotated 90 degrees clockwise.
The T2D Gold Standard does not provide classification of such tables as additional metadata.
Thus, the annotation for this table can not be used as is.

### 34501970_0_2477755352098394078.csv

#### Table Data

| "file"                                 | "size" | "date/time"         | "artist"                      | "title"                    | "year" | "album"                              | "comment"              | "length"  | "bi.." | "c.."  | "s.."  |
|----------------------------------------|--------|---------------------|-------------------------------|----------------------------|--------|--------------------------------------|------------------------|-----------|--------|--------|--------|
| "low_back_home_again.mp3"              | "5.1"  | "02.02.05 02:28:49" | "low mp3"                     | "back home again mp3"      | "NULL" | "badman winter 2001-2002 sample mp3" | "NULL"                 | "0:05:21" | "128"  | "s"    | "44"   |
| "clyde stubblefield - way back home.m" | "8.3"  | "02.05.16 15:06:28" | "NULL"                        | "NULL"                     | "NULL" | "NULL"                               | "NULL"                 | "0:08:41" | "128"  | "s"    | "44"   |
| "robert frith - the way back home.mp3" | "NULL" | "NULL"              | "NULL"                        | "NULL"                     | "NULL" | "NULL"                               | "NULL"                 | "NULL"    | "NULL" | "NULL" | "NULL" |
| "10 - listen to me.mp3"                | "3.3"  | "03.11.24 01:14:01" | "cleaver smith & swenson mp3" | "listen to me mp3"         | "NULL" | "back home again mp3"                | "NULL"                 | "NULL"    | "NULL" | "NULL" | "NULL" |
| "14 - the water is wide.mp3"           | "4.5"  | "03.11.24 01:23:06" | "cleaver smith & swenson mp3" | "the water is wide mp3"    | "NULL" | "back home again mp3"                | "NULL"                 | "NULL"    | "NULL" | "NULL" | "NULL" |
| "08 - queen of my heart.mp3"           | "2.4"  | "03.11.24 01:09:54" | "cleaver smith & swenson mp3" | "queen of my heart mp3"    | "NULL" | "back home again mp3"                | "NULL"                 | "NULL"    | "NULL" | "NULL" | "NULL" |
| "don_whaley_sing_me_back_home.mp3"     | "3.9"  | "02.03.05 16:57:36" | "artist mp3"                  | "track 07 mp3"             | "NULL" | "title mp3"                          | "NULL"                 | "0:04:09" | "128"  | "s"    | "44"   |
| "go_back_home_-_catch_me_when_i_fall." | "3.0"  | "NULL"              | "go back home mp3"            | "catch me when i fall mp3" | "NULL" | "NULL"                               | "NULL"                 | "0:03:12" | "128"  | "s"    | "44"   |
| "a_way_back_home.mp3"                  | "4.6"  | "00.04.02 21:02:35" | "voodoo sex stuff mp3"        | "a way back home mp3"      | "1999" | "NULL"                               | "www.voodoosexstuff.c" | "0:04:50" | "128"  | "s"    | "44"   |

#### Annotations

|                                              |          |         |     |
|----------------------------------------------|----------|---------|-----|
| "http://dbpedia.org/ontology/album"          | "album"  | "False" | "6" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "artist" | "True"  | "3" |
| "http://dbpedia.org/ontology/creationYear"   | "year"   | "False" | "5" |
| "http://dbpedia.org/ontology/Work/runtime"   | "length" | "False" | "8" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "title"  | "True"  | "4" |

#### Class Annotation

"34501970_0_2477755352098394078.tar.gz","Song","http://dbpedia.org/ontology/Song","0"

#### T2D Based RDF
```
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Song> .
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "low mp3" .
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "back home again mp3" .
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://dbpedia.org/ontology/creationYear> "NULL" .
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://dbpedia.org/ontology/album> "badman winter 2001-2002 sample mp3" .
<http://example.com/34501970_0_2477755352098394078.csv/1> <http://dbpedia.org/ontology/Work/runtime> "0:05:21" .
```

#### Comments

The table lists mp3 files for the songs.
Similar to "17769450_0_8003688464359007517.csv" T2D annotates "artist" and "title" columns with rdfs:label property.
While the table lists songs, this table contains two subject matters:
* mp3 file
* a musical work
Therefore, RDF can be modeled as:
* "file" is a subject column (rdfs:label), has "size", has "date/time", has "bitrate", has "sampling frequency", about song (no subject column) with "title", "artist", "year", "album", "length".

Originally, T2D ignores the information about mp3 file and only annotates information about a song.

### 37402655_0_9176587382722029523.csv

#### Table Data

| "nachname"          | "porto"          |
|---------------------|------------------|
| "vorname"           | "stefano"        |
| "künstlername"      | "-"              |
| "geburtsdatum"      | "-"              |
| "jahrgang"          | "1992"           |
| "grösse"            | "0"              |
| "nationalität"      | "italien"        |
| "position"          | "mittelfeld"     |
| "verein"            | "catania calcio" |
| "a-nationalspieler" | "nein"           |
| "webseite"          | "-"              |
| "zugriffe"          | "1694"           |

#### Annotations

|                                              |                |         |     |
|----------------------------------------------|----------------|---------|-----|
| "http://dbpedia.org/ontology/club"           | "verein"       | "False" | "8" |
| "http://dbpedia.org/ontology/birthYear"      | "jahrgang"     | "False" | "4" |
| "http://dbpedia.org/ontology/nickname"       | "künstlername" | "False" | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "nachname"     | "True"  | "0" |
| "http://dbpedia.org/ontology/nationality"    | "nationalität" | "False" | "6" |
| "http://dbpedia.org/ontology/birthDate"      | "geburtsdatum" | "False" | "3" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "vorname"      | "True"  | "1" |
| "http://dbpedia.org/ontology/Person/height"  | "grösse"       | "False" | "5" |

#### Class Annotation

"37402655_0_9176587382722029523.tar.gz","SoccerPlayer","http://dbpedia.org/ontology/SoccerPlayer","0"

#### T2D Based RDF
```
<http://example.com/37402655_0_9176587382722029523.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SoccerPlayer> .
<http://example.com/37402655_0_9176587382722029523.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "vorname" .
<http://example.com/37402655_0_9176587382722029523.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "stefano" .
<http://example.com/37402655_0_9176587382722029523.csv/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SoccerPlayer> .
<http://example.com/37402655_0_9176587382722029523.csv/2> <http://www.w3.org/2000/01/rdf-schema#label> "künstlername" .
<http://example.com/37402655_0_9176587382722029523.csv/2> <http://www.w3.org/2000/01/rdf-schema#label> "-" .
```

#### Comments

This table is similar to "2849108_0_5238405355789704342.csv".
According to [1] such tables should be classified as horizontal listings.
Identifying the row containing the subjects and predicates pose the biggest extraction challenge from this table type.
The header of a table is in the first column.
Before annotation and transformation to RDF such a table has to be rotated 90 degrees clockwise.
The T2D Gold Standard does not provide classification of such tables as additional metadata.
Thus, the annotation for this table can not be used as is.

### 38146710_0_3777366193503047044.csv

#### Table Data

| "network" | "affiliate" | "local channel" | "ird channel" | "broadcast format" |
|-----------|-------------|-----------------|---------------|--------------------|
| "abc"     | "kltv"      | "7"             | ""            | "hd"               |
| "abc"     | "kltv"      | "7"             | ""            | "digital"          |
| "cbs"     | "kytx"      | "19"            | ""            | "digital"          |
| "cbs"     | "kytx"      | "19"            | ""            | "hd"               |
| "cw"      | "kceb"      | "14"            | ""            | "digital"          |
| "fox"     | "kfxk"      | "51"            | ""            | "hd"               |
| "fox"     | "kfxk"      | "51"            | ""            | "digital"          |
| "ind"     | "ind"       | "18"            | ""            | "digital"          |
| "nbc"     | "ketk"      | "56"            | ""            | "hd"               |
| "nbc"     | "ketk"      | "56"            | ""            | "digital"          |
| "pbs"     | "pbs"       | "65"            | ""            | "digital"          |

#### Annotations

|                                              |                    |         |     |
|----------------------------------------------|--------------------|---------|-----|
| "http://dbpedia.org/ontology/pictureFormat"  | "broadcast format" | "False" | "4" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "network"          | "True"  | "0" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "affiliate"        | "True"  | "1" |

#### Class Annotation

"38146710_0_3777366193503047044.tar.gz","TelevisionStation","http://dbpedia.org/ontology/TelevisionStation","0"

#### T2D Based RDF
```
<http://example.com/38146710_0_3777366193503047044.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/TelevisionStation> .
<http://example.com/38146710_0_3777366193503047044.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "abc" .
<http://example.com/38146710_0_3777366193503047044.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "kltv" .
<http://example.com/38146710_0_3777366193503047044.csv/1> <http://dbpedia.org/ontology/pictureFormat> "hd" .
```

#### Comments

The table lists affiliates of the global broadcasting companies serving content in Tyler, Texas, United States (e.g. [KCEB](https://en.wikipedia.org/wiki/KCEB)).
The local companies can be identified by "affiliate" column, which makes it perfect candidate for rdfs:label.
However, "network" column is better annotated with "dbpedia-owl:affiliate" or "dbpedia-owl:parentCompany" property.
"local channel" can be possibly annotated with "dbpedia-owl:channel".

### 42846393_2_6922315287291245126.csv

#### Table Data

| "NOM"      | "PRENOM"        | "2000 Metres" | "VMA"  |
|------------|-----------------|---------------|--------|
| "CAROFF"   | "Arnaud"        | "7'02"        | "1706" |
| "VINE"     | "Djebbari"      | "7'52"        | "1526" |
| "LE FOLL"  | "Yvan"          | "7'55"        | "1516" |
| "ORIOL"    | "Lionel"        | "8'00"        | "1500" |
| "BOTHOREL" | "Christine"     | "8'13"        | "1461" |
| "GUILLERM" | "Yves"          | "8'23"        | "1432" |
| "LEON"     | "Thierry"       | "8'24"        | "1429" |
| "BOTHOREL" | "Yves"          | "8'30"        | "1412" |
| "MORVAN"   | "Raymond"       | "8'55"        | "1346" |
| "GARO"     | "Philippe"      | "9'03"        | "1326" |
| "MESSAGER" | "H?l?ne"        | "9'22"        | "1281" |
| "LE PAGE"  | "Lili"          | "9'23"        | "1279" |
| "CAROFF"   | "D?d?"          | "9'24"        | "1277" |
| "MESSAGER" | "Jean-No?l"     | "9'35"        | "1252" |
| "LE SAOUT" | "Marie-Th?r?se" | "10'10"       | "1180" |
| "GUYOMAR"  | "B?atrice"      | "1030"        | "1143" |

#### Annotations

|                                              |          |        |     |
|----------------------------------------------|----------|--------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "PRENOM" | "True" | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "NOM"    | "True" | "0" |

#### Class Annotation

"42846393_2_6922315287291245126.tar.gz","Athlete","http://dbpedia.org/ontology/Athlete","0"

#### T2D Based RDF
```
<http://example.com/42846393_2_6922315287291245126.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Athlete> .
<http://example.com/42846393_2_6922315287291245126.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "CAROFF" .
<http://example.com/42846393_2_6922315287291245126.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Arnaud" .
```

#### Comments

The table lists results of athletes on a particular competition.
"VMA" column can be possibly annotated with "dbpedia-owl:rank" property.
"2000 Metres" can be annotated by generic "[dbpedia-owl:runtime](http://dbpedia.org/ontology/runtime)" property.
Also, for first/last name [dbpedia-owl](http://dbpedia.org/ontology/personName) should be used.
In general case, for the persons FOAF vocabulary shall be used.
T2D annotating first/last names of a person as rdfs:label thus losing semantical meaning of the original concept.

### 47101798_1_4424372688353800689.csv

#### Table Data

| "&nbsp;" | "Name"                        | "Album"                    | "Time" | "Price" | "&nbsp;"         |
|----------|-------------------------------|----------------------------|--------|---------|------------------|
| "1"      | "Through It All"              | "Choose Your Battles - EP" | "4:12" | "?0.79" | "View In iTunes" |
| "2"      | "Light the Fuse and Run"      | "Choose Your Battles - EP" | "4:08" | "?0.79" | "View In iTunes" |
| "3"      | "Hit Me Like a Hurricane"     | "Choose Your Battles - EP" | "4:07" | "?0.79" | "View In iTunes" |
| "4"      | "Missing Out Moving On"       | "Choose Your Battles - EP" | "3:59" | "?0.79" | "View In iTunes" |
| "5"      | "Comebacks Aren't Your Thing" | "Choose Your Battles - EP" | "3:58" | "?0.79" | "View In iTunes" |
| "6"      | "Nobody's Looking At You"     | "Choose Your Battles - EP" | "3:22" | "?0.79" | "View In iTunes" |

#### Annotations

|                                              |         |         |     |
|----------------------------------------------|---------|---------|-----|
| "http://dbpedia.org/ontology/Work/runtime"   | "Time"  | "False" | "3" |
| "http://dbpedia.org/ontology/cost"           | "Price" | "False" | "4" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Album" | "True"  | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Name"  | "True"  | "1" |

#### Class Annotation

"47101798_1_4424372688353800689.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/47101798_1_4424372688353800689.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/47101798_1_4424372688353800689.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Through It All" .
<http://example.com/47101798_1_4424372688353800689.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Choose Your Battles - EP" .
<http://example.com/47101798_1_4424372688353800689.csv/1> <http://dbpedia.org/ontology/Work/runtime> "4:12" .
<http://example.com/47101798_1_4424372688353800689.csv/1> <http://dbpedia.org/ontology/cost> "?0.79" .
```

#### Comments
Similar to "17769450_0_8003688464359007517.csv" the table lists the songs from an album of an artist in an online shop.
The data can be modeled as RDF in two different ways, depending on a use case at the hand:
* The table is about songs. "Name" is a subject column (rdfs:label), included into "album", with duration "Time", "Price" and track number "" (i.e. first column).
* The table is about album. "Album" is a subject column (rdfs:label), which has track "Name" with "Time", "Price" and track number "" (i.e. first column)
* There is no subject column (i.e. artist is a subject). Then artist has released a track "Name", with track number "" (first row), included in an "Album", with duration "Time" and "Price".

T2D annotates both "Name" and "Album" as rdfs:label, which means that table corresponds to two different classes. It is controversial, because T2D annotates table with only one MusicalWork class.

### 48495038_0_1033305650426317920.csv

#### Table Data

| ""     | "" | "listen"                  | "music"      | "Album"           | "online" | "mp3"  | "Year" |
|--------|----|---------------------------|--------------|-------------------|----------|--------|--------|
| "NULL" | "" | "Another Sacrifice"       | "Life Cried" | "Banished Psalms" | "1"      | "3:54" | "2009" |
| "NULL" | "" | "Bloodstained"            | "Life Cried" | "Banished Psalms" | "2"      | "5:19" | "2009" |
| "NULL" | "" | "Dressed in Filth"        | "Life Cried" | "Banished Psalms" | "3"      | "4:30" | "2009" |
| "NULL" | "" | "Bound in Hate"           | "Life Cried" | "Banished Psalms" | "4"      | "4:38" | "2009" |
| "NULL" | "" | "Alone"                   | "Life Cried" | "Banished Psalms" | "5"      | "1:28" | "2009" |
| "NULL" | "" | "Preacher"                | "Life Cried" | "Banished Psalms" | "6"      | "7:09" | "2009" |
| "NULL" | "" | "More to Tarnish"         | "Life Cried" | "Banished Psalms" | "7"      | "5:19" | "2009" |
| "NULL" | "" | "Procession Rigor Mortis" | "Life Cried" | "Banished Psalms" | "8"      | "1:10" | "2009" |
| "NULL" | "" | "Solemn"                  | "Life Cried" | "Banished Psalms" | "9"      | "5:05" | "2009" |
| "NULL" | "" | "Forbidden"               | "Life Cried" | "Banished Psalms" | "10"     | "4:44" | "2009" |
| "NULL" | "" | "Derelict"                | "Life Cried" | "Banished Psalms" | "11"     | "1:47" | "2009" |

#### Annotations

|                                              |          |         |     |
|----------------------------------------------|----------|---------|-----|
| "http://dbpedia.org/ontology/Work/runtime"   | "mp3"    | "False" | "6" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "listen" | "True"  | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Album"  | "True"  | "4" |

#### Class Annotation

"48495038_0_1033305650426317920.tar.gz","Album","http://dbpedia.org/ontology/Album","0"

#### T2D Based RDF
```
<http://example.com/48495038_0_1033305650426317920.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Album> .
<http://example.com/48495038_0_1033305650426317920.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Another Sacrifice" .
<http://example.com/48495038_0_1033305650426317920.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Banished Psalms" .
<http://example.com/48495038_0_1033305650426317920.csv/1> <http://dbpedia.org/ontology/Work/runtime> "3:54" .
```
#### Comments
Similar to "17769450_0_8003688464359007517.csv" the table lists the songs from an album of an artist in an online shop.
In the case of this table, class corresponds to "Album", while property annotation include rdfs:label for both "Album" and "Song".
Moreover, "runtime" property corresponds to duration of a "Song", while it has to be duration of an "Album".

### 53264869_1_530811839053269226.csv

#### Table Data

| "file name"   | "file version"  | "file size" | "date"        | "time"  | "platform" | "sp requirement" | "service branch" |
|---------------|-----------------|-------------|---------------|---------|------------|------------------|------------------|
| "tcpmib.dll"  | "5.2.3790.4211" | "49152"     | "24-dec-2007" | "13:35" | "ia-64"    | "sp2"            | "not applicable" |
| "wtcpmib.dll" | "5.2.3790.4211" | "18432"     | "24-dec-2007" | "13:35" | "x86"      | "sp2"            | "wow"            |

#### Annotations

|                                                 |                |         |     |
|-------------------------------------------------|----------------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label"    | "file version" | "True"  | "1" |
| "http://dbpedia.org/ontology/Software/fileSize" | "file size"    | "False" | "2" |
| "http://dbpedia.org/ontology/computingPlatform" | "platform"     | "False" | "5" |
| "http://www.w3.org/2000/01/rdf-schema#label"    | "file name"    | "True"  | "0" |
| "http://dbpedia.org/ontology/date"              | "time"         | "False" | "4" |
| "http://dbpedia.org/ontology/date"              | "date"         | "False" | "3" |

#### Class Annotation

"53264869_1_530811839053269226.tar.gz","Software","http://dbpedia.org/ontology/Software","0"

#### T2D Based RDF
```
<http://example.com/53264869_1_530811839053269226.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Software> .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "tcpmib.dll" .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "5.2.3790.4211" .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://dbpedia.org/ontology/Software/fileSize> "49152" .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://dbpedia.org/ontology/date> "24-dec-2007" .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://dbpedia.org/ontology/date> "13:35" .
<http://example.com/53264869_1_530811839053269226.csv/1> <http://dbpedia.org/ontology/computingPlatform> "ia-64" .
```

#### Comments

The table lists DLL libraries.
Meaningful label is missing, therefore we argue that the table has no subject, i.e. talks about DLL libraries which have "file name", "version", "date", "time", "platform", "sp requirement" and "service branch".
While it make sense to merge "date" and "time" columns, this can not be done by annotating it with the same property (T2D), additional metadata is required for this annotation.
"file version" has rdfs:label in T2D, while the table is talking about "Software" (rdfs:label should be short human-readable description of the Software).

### 54802079_0_6709615660980454909.csv

#### Table Data

|                                                                                   |                                                                 |                |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------|
| "abeliophyllum                         distichum"                                 | "schneeforsythie                         wei&szlig;e forsythie" | "oleaceae"     |
| "abies                         alba"                                              | "wei&szlig;-tanne"                                              | "pinaceae"     |
| "abies                         balsamea"                                          | "balsam-tanne"                                                  | "pinaceae"     |
| "abies                         grandis"                                           | "k�sten-tanne                         riesen-tanne"             | "pinaceae"     |
| "abies                         koreana"                                           | "korea-tanne"                                                   | "pinaceae"     |
| "abies                         pinsapo 'glauca'"                                  | "blaue                         spanische tanne"                 | "pinaceae"     |
| "abies                         procera"                                           | "pazifische                         edel-tanne"                 | "pinaceae"     |
| "abromeitiella                         brevifolia"                                | "&nbsp;"                                                        | "bromeliaceae" |
| "abromeitiella                         lorentziana (= deuterocohnia lorentziana)" | "&nbsp;"                                                        | "bromeliaceae" |
| "abutilon                         megapotamicum"                                  | "&nbsp;"                                                        | "malvaceae"    |

#### Annotations

|                                              |                                         |        |     |
|----------------------------------------------|-----------------------------------------|--------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "schneeforsythie wei&szlig;e forsythie" | "True" | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "abeliophyllum distichum"               | "True" | "0" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "oleaceae"                              | "True" | "2" |

#### Class Annotation

"54802079_0_6709615660980454909.tar.gz","Plant","http://dbpedia.org/ontology/Plant",""

#### T2D Based RDF
```
<http://example.com/54802079_0_6709615660980454909.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Plant> .
<http://example.com/54802079_0_6709615660980454909.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "abeliophyllum distichum" .
<http://example.com/54802079_0_6709615660980454909.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "schneeforsythie wei&szlig;e forsythie" .
<http://example.com/54802079_0_6709615660980454909.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "oleaceae" .
```

#### Comments
This table is similar to 24003697_0_8569423605161973748.csv in sense that it maps all of the columns to rdfs:label.
The table talks about plants and includes Latin name of the plant in the first column, German name in the second column and plant family in the last column.
Given that the table is mapped to German subset of DBpedia, German name should be selected as subject column (i.e. rdfs:label), for example, "schneeforsythie weisse forsythie", while the first column would correspond to "scientificName" property and the third column will be "dbo:family".
Annotating all three columns as rdfs:label is incorrect.

### 60884685_1_5420701306478974044.csv

#### Table Data

| "&nbsp;" | "Name"                        | "Album"                                                      | "Time" | "Price" | "&nbsp;"         |
|----------|-------------------------------|--------------------------------------------------------------|--------|---------|------------------|
| "1"      | "LvUrFR3NZ"                   | "Halo 3 (Original Soundtrack)"                               | "2:18" | "$0.99" | "View In iTunes" |
| "2"      | "Florida (Cosmic Kids Remix)" | "Florida - Single"                                           | "6:45" | "$0.99" | "View In iTunes" |
| "3"      | "The Waves"                   | "Bloomsbury - EP"                                            | "3:16" | "$0.99" | "View In iTunes" |
| "4"      | "Leonard Woolf"               | "Bloomsbury - EP"                                            | "4:00" | "$0.99" | "View In iTunes" |
| "5"      | "Ms. Bentwich"                | "Bloomsbury - EP"                                            | "3:18" | "$0.99" | "View In iTunes" |
| "6"      | "Eminent Victorians"          | "Bloomsbury - EP"                                            | "2:22" | "$0.99" | "View In iTunes" |
| "7"      | "Florida"                     | "Florida - Single"                                           | "4:23" | "$0.99" | "View In iTunes" |
| "8"      | "Calypso Gold"                | "Cocoon Of Love"                                             | "3:44" | "$0.99" | "View In iTunes" |
| "9"      | "Clamoring for Your Heart"    | "Clamoring for Your Heart / This Weather a Swimmer - Single" | "5:34" | "$0.99" | "View In iTunes" |
| "10"     | "Sadie &amp; Andy"            | "Cocoon Of Love"                                             | "3:36" | "$0.99" | "View In iTunes" |

#### Annotations

|                                              |         |         |     |
|----------------------------------------------|---------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "Album" | "True"  | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Name"  | "True"  | "1" |
| "http://dbpedia.org/ontology/Work/runtime"   | "Time"  | "False" | "3" |
| "http://dbpedia.org/ontology/cost"           | "Price" | "False" | "4" |

#### Class Annotation

"60884685_1_5420701306478974044.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/60884685_1_5420701306478974044.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/60884685_1_5420701306478974044.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "LvUrFR3NZ" .
<http://example.com/60884685_1_5420701306478974044.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Halo 3 (Original Soundtrack)" .
<http://example.com/60884685_1_5420701306478974044.csv/1> <http://dbpedia.org/ontology/Work/runtime> "2:18" .
<http://example.com/60884685_1_5420701306478974044.csv/1> <http://dbpedia.org/ontology/cost> "$0.99" .
```

#### Comments

This table is similar to 17769450_0_8003688464359007517.csv. What is surpising, that T2D includes dbo:cost property annotation in this table, but does not include it in 17769450_0_8003688464359007517.csv (which also contains cost column).
RDF data can be modeled with a "Song" or an "Album" as main subject. However, T2D uses rdfs:label for both of them, which is an annotation mistake.

### 61108455_0_4273649346480472385.csv

#### Table Data

| "street"                | "type"         | "city"         | "state" | "zip"   | "expires"    | "beds" | "baths" | "sq. ft." | "util. paid" | "w/d" | "garage" | "rent"  | "deposit" | "option to buy" | "virtual tour"                | "application" |
|-------------------------|----------------|----------------|---------|---------|--------------|--------|---------|-----------|--------------|-------|----------|---------|-----------|-----------------|-------------------------------|---------------|
| "127 felix street"      | "sfh"          | "georgetown"   | "ky"    | "40324" | "now"        | "3"    | "2"     | "1232"    | "-"          | "h/u" | "2"      | "$925"  | "$925"    | "yes"           | "view tour            &nbsp;" | "&nbsp;"      |
| "1352 royalty court #6" | "apt"          | "lexington"    | "ky"    | "40504" | "now"        | "2"    | "1"     | "725"     | "water"      | "h/u" | "n/a"    | "$525"  | "$525"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "467 johnson ave"       | "sfh"          | "lexington"    | "ky"    | "40508" | "now"        | "2"    | "1"     | "1300"    | "-"          | "yes" | "none"   | "$950"  | "$950"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "1344 royalty court #4" | "apt"          | "lexington"    | "ky"    | "40504" | "now"        | "2"    | "1"     | "725"     | "water"      | "h/u" | "n/a"    | "$525"  | "$525"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "2076 patriot way"      | "sfh"          | "independence" | "ky"    | "41051" | "2014/06/30" | "4"    | "2.5"   | "2300"    | "-"          | "h/u" | "2"      | "$1595" | "$3000"   | "yes"           | "view tour            &nbsp;" | "&nbsp;"      |
| "343 aylesford pl"      | "sfh - campus" | "lexington"    | "ky"    | "40508" | "2013/07/31" | "7"    | "3"     | "2480"    | "-"          | "yes" | "n/a"    | "$2500" | "$2500"   | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "1352 royalty court #1" | "apt"          | "lexington"    | "ky"    | "40504" | "2013/02/28" | "1"    | "1"     | "675"     | "water"      | "h/u" | "n/a"    | "$450"  | "$450"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "627 sherard circle"    | "duplex"       | "lexington"    | "ky"    | "40517" | "2013/01/31" | "3"    | "2.5"   | "1400"    | "-"          | "yes" | "1"      | "$850"  | "$850"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |
| "1352 royalty court #3" | "apt"          | "lexington"    | "ky"    | "40504" | "2012/12/31" | "1"    | "1"     | "675"     | "water"      | "h/u" | "n/a"    | "$450"  | "$450"    | "no"            | "view tour            &nbsp;" | "&nbsp;"      |

#### Annotations

|                                                  |           |         |     |
|--------------------------------------------------|-----------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label"     | "city"    | "True"  | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label"     | "street"  | "True"  | "0" |
| "http://dbpedia.org/ontology/federalState"       | "state"   | "False" | "3" |
| "http://dbpedia.org/ontology/Building/floorArea" | "sq. ft." | "False" | "8" |
| "http://dbpedia.org/ontology/zipCode"            | "zip"     | "False" | "4" |
| "http://dbpedia.org/ontology/bedCount"           | "beds"    | "False" | "6" |

#### Class Annotation

"61108455_0_4273649346480472385.tar.gz","Thing","http://www.w3.org/2002/07/owl#Thing","0"

#### T2D Based RDF
```
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Thing> .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "127 felix street" .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "georgetown" .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://dbpedia.org/ontology/federalState> "ky" .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://dbpedia.org/ontology/zipCode> "40324" .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://dbpedia.org/ontology/bedCount> "3" .
<http://example.com/61108455_0_4273649346480472385.csv/1> <http://dbpedia.org/ontology/Building/floorArea> "1232" .
```

#### Comments
The table lists the deals for the real estate, which is "dbo:Sales" class in DBpedia ontology.
"dbo:Thing" class is a superclass of everything and does not provide any semantic meaning for a subject.
"dbo:Sales" expires on "expires" and is about property of type "type", located on "street", "city", "state", "zip", with number of "beds", "baths", "sq. ft.", and additional information "util. paid", "w/d", "garage", "rent", "deposit", "option to buy", "virtual tour", "application".
"street" and "city" should be modeled with "dbo:locatedIn" property (possibly with blank node).
Annotating location with rdfs:label in this case is incorrect.

### 63198107_0_5688435789215389159.csv

#### Table Data

| "&nbsp;" | "Name"                                          | "Album"                                                  | "Time" | "Price" | "&nbsp;"         |
|----------|-------------------------------------------------|----------------------------------------------------------|--------|---------|------------------|
| "1"      | "No Guarantees (Money Back) [Shorter]"          | "No Guarantees (Money Back) - Single"                    | "3:23" | "$0.99" | "View In iTunes" |
| "2"      | "No Guarantees (Money Back) [Longer]"           | "No Guarantees (Money Back) - Single"                    | "4:28" | "$0.99" | "View In iTunes" |
| "3"      | "No Guarantees (Money Back) [Longer]"           | "Tomorrow: Electro"                                      | "4:28" | "$0.99" | "View In iTunes" |
| "4"      | "Prisoners of Our Own Devices (Original Mix)"   | "Prisoners of Our Own Devices - Single"                  | "6:46" | "$0.99" | "View In iTunes" |
| "5"      | "No Guarantees (Money Back) [Longer]"           | "Prisoners of Our Own Devices - Single"                  | "4:28" | "$0.99" | "View In iTunes" |
| "6"      | "Dominican Girls (Las Matas de Santa Cruz Mix)" | "Dominican Girls (Las Matas de Santa Cruz Mix) - Single" | "6:34" | "$0.99" | "View In iTunes" |

#### Annotations

|                                              |         |         |     |
|----------------------------------------------|---------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "Name"  | "True"  | "1" |
| "http://dbpedia.org/ontology/Work/runtime"   | "Time"  | "False" | "3" |
| "http://dbpedia.org/ontology/cost"           | "Price" | "False" | "4" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Album" | "True"  | "2" |

#### Class Annotation

"63198107_0_5688435789215389159.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/63198107_0_5688435789215389159.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/63198107_0_5688435789215389159.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "No Guarantees (Money Back) [Shorter]" .
<http://example.com/63198107_0_5688435789215389159.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "No Guarantees (Money Back) - Single" .
<http://example.com/63198107_0_5688435789215389159.csv/1> <http://dbpedia.org/ontology/Work/runtime> "3:23" .
<http://example.com/63198107_0_5688435789215389159.csv/1> <http://dbpedia.org/ontology/cost> "$0.99" .
```

#### Comments

This table is similar to 17769450_0_8003688464359007517.csv. What is surpising, that T2D includes dbo:cost property annotation in this table, but does not include it in 17769450_0_8003688464359007517.csv (which also contains cost column).
RDF data can be modeled with a "Song" or an "Album" as main subject. However, T2D uses rdfs:label for both of them, which is an annotation mistake.

### 78616821_0_2458612333287914096.csv

#### Table Data

| "&nbsp;" | "Name"                 | "Artist"        | "Time" | "Price" | "&nbsp;"         |
|----------|------------------------|-----------------|--------|---------|------------------|
| "1"      | "Over You"             | "Honor Society" | "3:04" | "$0.99" | "View In iTunes" |
| "2"      | "Full Moon Crazy"      | "Honor Society" | "3:07" | "$0.99" | "View In iTunes" |
| "3"      | "My Own Way"           | "Honor Society" | "3:38" | "$0.99" | "View In iTunes" |
| "4"      | "Two Rebels"           | "Honor Society" | "3:31" | "$0.99" | "View In iTunes" |
| "5"      | "Why Didn't I"         | "Honor Society" | "3:45" | "$0.99" | "View In iTunes" |
| "6"      | "Goodnight My Love"    | "Honor Society" | "3:32" | "$0.99" | "View In iTunes" |
| "7"      | "Here Comes Trouble"   | "Honor Society" | "3:16" | "$0.99" | "View In iTunes" |
| "8"      | "See U In the Dark"    | "Honor Society" | "3:06" | "$0.99" | "View In iTunes" |
| "9"      | "Nobody Has to Know"   | "Honor Society" | "2:53" | "$0.99" | "View In iTunes" |
| "10"     | "Sing for You"         | "Honor Society" | "3:44" | "$0.99" | "View In iTunes" |
| "11"     | "Rock With You"        | "Honor Society" | "3:44" | "$0.99" | "View In iTunes" |
| "12"     | "Don't Close the Book" | "Honor Society" | "4:09" | "$0.99" | "View In iTunes" |
| "13"     | "Where Are You Now"    | "Honor Society" | "3:49" | "$0.99" | "View In iTunes" |

#### Annotations

|                                              |          |         |     |
|----------------------------------------------|----------|---------|-----|
| "http://dbpedia.org/ontology/Work/runtime"   | "Time"   | "False" | "3" |
| "http://dbpedia.org/ontology/cost"           | "Price"  | "False" | "4" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Artist" | "True"  | "2" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Name"   | "True"  | "1" |

#### Class Annotation

"78616821_0_2458612333287914096.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/78616821_0_2458612333287914096.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/78616821_0_2458612333287914096.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Over You" .
<http://example.com/78616821_0_2458612333287914096.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Honor Society" .
<http://example.com/78616821_0_2458612333287914096.csv/1> <http://dbpedia.org/ontology/Work/runtime> "3:04" .
<http://example.com/78616821_0_2458612333287914096.csv/1> <http://dbpedia.org/ontology/cost> "$0.99" .
```
#### Comments

This table is similar to 17769450_0_8003688464359007517.csv. What is surpising, that T2D includes dbo:cost property annotation in this table, but does not include it in 17769450_0_8003688464359007517.csv (which also contains cost column).
RDF data can be modeled with a "Song" or an "Artist" as main subject. However, T2D uses rdfs:label for both of them, which is an annotation mistake.

### 80992694_0_3506971500806631353.csv

#### Table Data

| "Competition"                      | "Event"                  | "Year"   | "Time"    | "Medal/Position" |
|------------------------------------|--------------------------|----------|-----------|------------------|
| "Olympic Games"                    | "200m Freestyle"         | "2008"   | "1:47.47" | "8th"            |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7:05.92" | "6th"            |
| "World Championships"              | "200m Freestyle"         | "2011"   | "1:47.89" | "12th"           |
| "&nbsp;"                           | "400m Freestyle"         | "&nbsp;" | "3:49.91" | "18th"           |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7:10.84" | "6th"            |
| "&nbsp;"                           | "400m Freestyle"         | "2009"   | "3:46.75" | "14th"           |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7:05.67" | "7th"            |
| "&nbsp;"                           | "400m Freestyle"         | "2007"   | "3.50.07" | "15th"           |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7.11.28" | "4th"            |
| "Commonwealth Games"               | "200m Freestyle"         | "2010"   | "1:47.88" | "GOLD"           |
| "&nbsp;"                           | "400m Freestyle"         | "&nbsp;" | "3:51.74" | "6th"            |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7:14.02" | "SILVER"         |
| "&nbsp;"                           | "200m Freestyle"         | "2006"   | "1.50.50" | "14th"           |
| "&nbsp;"                           | "400m Freestyle"         | "&nbsp;" | "3.52.69" | "6th"            |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7.14.40" | "SILVER"         |
| "European Championships"           | "200m Freestyle"         | "2010"   | "1:47.60" | "5th"            |
| "&nbsp;"                           | "400m Freestyle"         | "&nbsp;" | "3:49.13" | "6th"            |
| "&nbsp;"                           | "4x200m Freestyle Relay" | "&nbsp;" | "7:16.33" | "4th"            |
| "&nbsp;"                           | "200m Freestyle"         | "2006"   | "1.49.55" | "13th"           |
| "&nbsp;"                           | "400m Freestyle"         | "&nbsp;" | "3.53.63" | "20th"           |
| "World Short Course Championships" | "400m Freestyle"         | "2008"   | "3:40.22" | "BRONZE"         |
| "European Junior Championships"    | "200m Freestyle"         | "2006"   | "1.49.26" | "GOLD"           |
| "&nbsp;"                           | "4x100m Freestyle Relay" | "&nbsp;" | "3.25.59" | "SILVER"         |
| "&nbsp;"                           | "4x100m Medley Relay"    | "&nbsp;" | "3.48.88" | "BRONZE"         |
| "&nbsp;"                           | "400m Freestyle"         | "2005"   | "3.55.18" | "SILVER"         |

#### Annotations

|                                              |                  |         |     |
|----------------------------------------------|------------------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "Event"          | "True"  | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Competition"    | "True"  | "0" |
| "http://dbpedia.org/ontology/rank"           | "Medal/Position" | "False" | "4" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "Year"           | "True"  | "2" |

#### Class Annotation

"80992694_0_3506971500806631353.tar.gz","SportCompetitionResult","http://dbpedia.org/ontology/SportCompetitionResult","0"

#### T2D Based RDF
```
<http://example.com/80992694_0_3506971500806631353.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SportCompetitionResult> .
<http://example.com/80992694_0_3506971500806631353.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "Olympic Games" .
<http://example.com/80992694_0_3506971500806631353.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "200m Freestyles" .
<http://example.com/80992694_0_3506971500806631353.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "2008" .
<http://example.com/80992694_0_3506971500806631353.csv/1> <http://dbpedia.org/ontology/rank> "8th" .
```

#### Comments

The table lists personal results of Michael Phelps in various competitions.
The subject matter is a "Result", accomplished at "Competition", in a category "Event", in a "Year", with the "Time", and where athlete got "Medal/Position".
T2D annotates 3 columns with rdfs:label ("Event", "Competition" and "Year"), thus losing semantical meaning of the original concept.

### 83577589_0_3008022348570648346.csv

#### Table Data

| "id:"               | "101179"              |
|---------------------|-----------------------|
| "name:"             | "an ocean bed ep"     |
| "artist:"           | "absolute time"       |
| "label:"            | "filtro"              |
| "catalog:"          | "[filtro.017]"        |
| "media format:"     | "file"                |
| "country:"          | "mexico"              |
| "released:"         | "2006-04-28"          |
| "mixed:"            | "&nbsp;"              |
| "credits:"          | "&nbsp;"              |
| "notes:"            | "&nbsp;"              |
| "sumitted by:"      | "maitreya"            |
| "entry created:"    | "2010-02-13 19:53:18" |
| "update history:"   | "NULL"                |
| "in my favorites:"  | "NULL"                |
| "in my collection:" | "NULL"                |

#### Annotations

|                                              |             |         |     |
|----------------------------------------------|-------------|---------|-----|
| "http://www.w3.org/2000/01/rdf-schema#label" | "name:"     | "True"  | "1" |
| "http://www.w3.org/2000/01/rdf-schema#label" | "artist:"   | "True"  | "2" |
| "http://dbpedia.org/ontology/country"        | "country:"  | "False" | "6" |
| "http://dbpedia.org/ontology/releaseDate"    | "released:" | "False" | "7" |
| "http://dbpedia.org/ontology/recordLabel"    | "label:"    | "False" | "3" |

#### Class Annotation

"83577589_0_3008022348570648346.tar.gz","MusicalWork","http://dbpedia.org/ontology/MusicalWork","0"

#### T2D Based RDF
```
<http://example.com/83577589_0_3008022348570648346.csv/1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/83577589_0_3008022348570648346.csv/1> <http://www.w3.org/2000/01/rdf-schema#label> "101179" .
<http://example.com/83577589_0_3008022348570648346.csv/2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/MusicalWork> .
<http://example.com/83577589_0_3008022348570648346.csv/2> <http://www.w3.org/2000/01/rdf-schema#label> "an ocean bed ep" .
```

#### Comments
According to [1] such tables should be classified as horizontal listings.
Identifying the row containing the subjects and predicates pose the biggest extraction challenge from this table type.
The header of a table is in the first column.
Before annotation and transformation to RDF such a table has to be rotated 90 degrees clockwise.
The T2D Gold Standard does not provide classification of such tables as additional metadata.
Thus, the annotation for this table can not be used as is.

## Literature

[1] [Crestan, Eric, and Patrick Pantel. "Web-scale table census and classification." Proceedings of the fourth ACM international conference on Web search and data mining. ACM, 2011.](http://www.patrickpantel.com/download/papers/2011/wsdm11.pdf)
