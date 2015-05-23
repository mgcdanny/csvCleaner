[![Build Status](https://travis-ci.org/mgcdanny/csvCleaner.svg?branch=master)](https://travis-ci.org/mgcdanny/csvCleaner)


TODO: add option to include / exclude header row... now it assumes a header row exists always

To make this a 'true' command line tool:


Copy and paste this line into the terminal where csv_cleaner.py is located:


cp csv_cleaner.py csv_cleaner && chmod 0744 csv_cleaner && cp csv_cleaner /usr/local/bin/


Then from any directory with your csv file:


$  csv_cleaner -i  my_dirty_csv.csv

Note:

A 'dirty' csv is one where the number of columns per row is inconsistent.  For example, if the first row of the csv file (typically the header) is 10 columns then we would expect the rest of the csv file to have 10 columns per row.  If there are more or less than 10, the csv parser you are using will likely have issues.  This script will put all rows of the same lenght into a designated file.  For example out_10.csv will have all the rows with 10 columns,  while out_8.csv will have all the rows with 8 columns.

