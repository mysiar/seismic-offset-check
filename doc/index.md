# Seismic Offset Check

### Database operations
1. create DB: menu _**DB->Create DB**_ - creates SQLite DB file and table structure
2. update DB: menu _**DB->Update DB**_ - select DB to update and all SPS files you want to load (preplot, operation plan, etc)

### Check
1. select DB
2. select SPS file
3. set Easting & Northing limits accordingly
3. Run

Output files are created in the same folder where SPS file is.

There are 2 types of output files:
* **.check.csv** - contains all checked records with Easting & Northing diffs and error flags accordingly to limit
* **.not-in-db.csv** - contains all records that could not be find in DB