# Python Projects

**Table of Contents**

- [Current Tasks](#current-tasks)
- [Current Errors and Pressing Tasks](#current-errors-and-pressing-tasks)
- [Projects](#projects)
  -[Data Generator](#data-generator-dg)
- [Required Python Modules](#required-python-modules)
- [Running Scripts](#running-scripts)
  - [Data Generator Script](#data-generator-data_generator_script)
- [Deprecated Scripts](#deprecated-scripts)
- [Completed Tasks](#completed-tasks)
- [Resolved Errors](#resolved-errors)



# Current Tasks

- [ ] Set up and decide on modules for data generator


- [ ] Random data
    - [x] datetime (7/29/2017)
      - [x] UNIXTime (7/29/2017)
      - [ ] Julian Day
      - [x] Day of year (7/30/2017)
      - [ ] Different date sequence Y-D-M
    - [x] names (7/29/2017)
      - [x] load names from file (7/29/2017)
    - [x] emails (7/29/2017)
    - [x] payload (7/29/2017)
    - [x] latitude/longitude (7/29/2017)
      - [x] latitude/longitude checker (7/29/2017)


- [ ] Push data into pandas DataFrame
    - [ ] Output data in different formats
        - [ ] JSON
        - [ ] xml
        - [ ] pickle
        - [x] csv (7/29/2017)
        - [ ] cdf
        - [x] ascii (delimited by a tab)
        

- [ ] Input statements
    - [ ] Format of data
        - [ ] Output datetime column in various formats
    - [x] Different delimiters (i.e ;/,/./*&/%!) (7/31/2017)

- [ ] Add random corruption
    - [ ] Column-wise
    - [ ] DataFrame-wise

- [ ] Statements to break script
    - [ ] Inputs that will trigger errors


# Current Errors and Pressing Tasks

### Output to SQL
- Create a connection and execute procedures from the pandas dataframe to sql. The function from the dataframe will be .to_sql, but requires a connection method. Just specifying an output name does not suffice as in the .to_csv function.  
```TypeError: to_sql() missing 1 required positional argument: 'con'```

### Adding corruption
- Specific amount of corruption will be specified with an input statement. A total amount of elements within the frame will be calculated and a random percentage will be replaced with corrupted values. Functions should include 1) find number of elements, 2) randomize element location/index, 3) find and replace element values.



# Projects

## Data Generator (DG)

Columns       | Format | Notes
------------ | ------------- | -------------
**names**     | random string |  Load from a file 'names.txt' and push into a list/set of full string.
**emails**    | random string with @host.com | First initial of first name, followed by last name '@' host '.' com/edu/gov/etc.
**from ip**   | formatted sequence with '.' (i.e ##.###.###.###) | Sequence of integers separated by '.', usually in the format (##.###.###.###).
**to ip**     | formatted sequence with '.' (i.e ##.###.###.###) | Sequence of integers separated by '.', usually in the format (##.###.###.###).
**latitude**  | formatted float, 1-round from (0-360) | Formatted float followed by a decimal of latitude (-90 to 90 degrees) and longitude (-180 to 180).
**longitude** | formatted float, 1-round from (0-360) | Formatted float followed by a decimal of latitude (-90 to 90 degrees) and longitude (-180 to 180).
**datetime**  | datetime | Common string yyyy-mm-dd hh:mm:ss.s and convert using datetime functions.
**payload**| random integer                | A random integer from 0-1000000.
** **| -                | -           | -
** **| -                | -           | -

#### Corruption
- Values that are 'bad' (i.e -99999, null, nan, -1E30)
- Push to random spots in column and whole DataFrame
- Set up extent of corruption (i.e harsh (70% of data), light (20% of data))



### Required Python Modules
Module       | Submodule(s) | as | Uses
------------ | ------------- | ------------- | -------------
**pandas**              | -                | pd          | DataFrames, indexing, plotting, downloading http url data, csv_reader()
**numpy**               | -                | np          | NaN values
~~**spacepy**~~             | pycdf            | -           | Reading Common Data Format
~~**urllib**~~              | error            | -           | For HTTPError recognition
**random**              | -                | -           | Randomizer for random colors
~~**matplotlib**~~          | .pyplot, .mdates | plt, mdates | Plotting, subplots, date formatting
**datetime**            | -                | -           | Datetime indexing, datetime strings, datetime conversion from strings
**sys**                 | -                | -           | Exiting script
~~**wget**~~                | -                | -           | Downloading files online (.cdf, .csv, .ascii, .txt)
~~**os**~~                  | -                | -           | Remove files through script
**geopy.geocoders**     | Nominatim        | -           | Enables realtime verification of given latitudes and longitudes

\* Strike through modules are currently not in use in the current version of the script, but will later be implemented.

# Running Scripts

### Data Generator ([data_generator_script](https://github.com/byamashiro/Python_Projects/blob/master/data_generator.py))

In [31]: run data_generator.py  
\========================================  
\=            Data Generator            =  
\========================================  
Enter desired number of lines: 30  
[x] Data Frame Generated.  
[x] Names generated.  
Enter a start date (yyyymmdd): 20110307  
Enter an end date (yyyymmdd): 20120105  
Enter a start hour (hh): 01  
Enter an end hour (hh): 20  
[x] Dates generated.  
[x] Email addresses generated.  
[x] IP Addresses generated.  
Check Latitude and Longitude (yes or no) - use "no" for time saving: no  
[x] Latitude and longitude generated.  
[x] Payload generated.  
\========================================  
\=            Output Options            =  
\========================================  
1 - .csv  
2 - .txt  
3 - .JSON (currently unavailable)  
4 - .pickle (currently unavailable)  
5 - .sql (currently unavailable)  
\========================================  
Enter Output Option(s) then "done": 1  
Enter Output Option(s) then "done": 2  
Enter Output Option(s) then "done": done  
Choose delimiter character for .csv output: ,  
[x] Output as CSV generated.  
[x] Output as TXT generated.


#### Sample Generated Data

fname | lname | date_time | unix_time | doy | email_address | toip |  fmip |  lat | long |  payload
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Vonda  | Bossart | 3/14/11 11:06 | 1300136783 | 3  |   VBossart@mail2chuck.com | 78.69.169.59   | 168.163.120.28 | -50.80011  | -158.215686 | 181288
Sade   | Polan   | 4/2/11 19:13  | 1301807584 | 73 |   SPolan@timein.net       | 230.19.28.105  | 240.53.187.8   | -77.46244  | -75.203543  | 437522
Leatha | Haran   | 4/3/11 14:29  | 1301876956 | 92 |   LHaran@mail2liberia.com | 27.107.202.74  | 13.218.216.247 | -64.362629 | 168.564349  | 334732

##### .csv output
```
fname,lname,date_time,unix_time,doy,email_address,toip,fmip,lat,long,payload  
Vonda,Bossart,2011-03-14 11:06:23,1300136783.0,3,VBossart@mail2chuck.com,78.69.169.59,168.163.120.28,-50.80011,-158.215686,181288  
Sade,Polan,2011-04-02 19:13:04,1301807584.0,73,SPolan@timein.net,230.19.28.105,240.53.187.8,-77.46244,-75.203543,437522  
Leatha,Haran,2011-04-03 14:29:16,1301876956.0,92,LHaran@mail2liberia.com,27.107.202.74,13.218.216.247,-64.362629,168.564349,334732  
...
```

##### .txt output
```
fname lname date_time unix_time doy email_address toip  fmip  lat long  payload  
Vonda Bossart 2011-03-14 11:06:23 1300136783.0  3 VBossart@mail2chuck.com 78.69.169.59  168.163.120.28  -50.80011 -158.215686 181288  
Sade  Polan 2011-04-02 19:13:04 1301807584.0  73  SPolan@timein.net 230.19.28.105 240.53.187.8  -77.46244 -75.203543  437522  
Leatha  Haran 2011-04-03 14:29:16 1301876956.0  92  LHaran@mail2liberia.com 27.107.202.74 13.218.216.247  -64.362629  168.564349  334732  
...
```


[//]: <> <img src="Plots/omni_test.png" width="600">




# Deprecated Scripts
 

# Completed Tasks

# Resolved Errors

