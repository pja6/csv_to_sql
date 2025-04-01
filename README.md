# csv_to_sql

### So, turns out you can't just import csv files into MySQL Workbench for security reasons!

Made this small python program that converts a single csv file into a .sql file that has an insert statement for each row.

Currently only works for one table at a time, but maybe I'll update it later - also keep in mind if there is a UNIQUE attribute in your table and your tuples 
contain empty cells, they will default to "NULL" but the UNIQUE column will still flag them as the same since there's not a simple way to write null to the 
file without quotes.

To use, drop the python file in the same directory as your csv files and use:

    python3 sqlinsert.py <csv_file> <table_name> <optional: sql_file_name>

    
