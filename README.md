data models
===========

This repository holds json examples and their respective Pydantic data models that are representative of the documents stored in each collection of our mongo database. These are the documents our mxdb-server REST-API will be creating, reading, updating and deleting.

The following documentation will display the database and collection (db.Collection) and then each document type it holds as a dot point with a description.

mxdata.Adp
==========

* <b>screening</b>: data model for screening data collections that are used to calculate collection strategies (mosFLM)

* <b>standard</b>: data model for standard Adp processing. This comes in 3 flavours for the 3 processing options (gopy, xia2dials, autoPROC)

* <b>native-sad</b>: data model for multi-orientation dataset collections for the 1 sample (single scan request, multiple datasets collected). Multiple native-sad entries in Adp. MergeId used for sxdm merging and the first dataset is used as reference (results in Adm collection).

<h3>Adp methods supported</h3> 
"screening"
"standard"
"standard-repeat"
"bookmarks"
"native-sad"
"serial-xtal"
"inverse-beam"
"interleave-no-inverse"
"interleave-and-inverse-first"
"interleave-and-inverse-all"


mxdata.Datasets
===============

* <b>native-sad</b>: multi-orientation dataset collection from a single scan request. Each collection at a different orientation is processed separately. 

WIP... much more to come




Contributors
============
* Jakub Kaminski
* Justyna Wojdyla
* Ezequiel Panepucci
* Kate Smith