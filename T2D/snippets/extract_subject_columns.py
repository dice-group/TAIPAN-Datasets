#!/usr/bin/env python

from __future__ import print_function
import os
import re
import string

PROPERTY_MAPPINGS_FOLDER = "../attributes_complete/"
REGEX_TRUE = re.compile(".*true.*", re.I)

path, dirs, property_mapping_files = os.walk(PROPERTY_MAPPINGS_FOLDER).next()

subject_columns = []

for property_mapping_file in property_mapping_files:
    f = open(os.path.join(path, property_mapping_file), 'rU')
    no_subject_column = True
    for line in f.readlines():
        property_uri, column_header, is_key, column_index = map(lambda x: re.sub(r'"', '', x), line.split(","))
        if REGEX_TRUE.match(is_key):
            subject_columns.append({
                "table_id": property_mapping_file,
                "subject_column": string.strip(column_index)
            })
            no_subject_column = False
            print("%s, %s" % (property_mapping_file, column_index), end="")
    if no_subject_column:
        subject_columns.append({
            "table_id": property_mapping_file,
            "subject_column": "-1"
        })
