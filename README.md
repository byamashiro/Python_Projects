# Python Projects

**Table of Contents**

- [Current Tasks](#current-tasks)
- [Current Errors and Pressing Tasks](#current-errors-and-pressing-tasks)
- [Projects](#projects)
- [Required Python Modules](#required-python-modules)
- [Running Scripts](#running-scripts)
- [Deprecated Scripts](#deprecated-scripts)
- [Data](#data)
  - [Data Caveats](#data-caveats)
  - [Data Originals](#data-originals)
  - [Sample Data](#sample-data)
- [Completed Tasks](#completed-tasks)
- [Resolved Errors](#resolved-errors)



# Current Tasks

- [ ] Set up and decide on modules for data generator


- [ ] Random data
    - [x] datetime (7/29/2017)
      - [x] UNIXTime (7/29/2017)
      - [ ] Julian Day
      - [ ] Day of year
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
    - [ ] Different delimiters (i.e ;/,/./*&/%!)

- [ ] Add random corruption
    - [ ] Column-wise
    - [ ] DataFrame-wise


# Current Errors and Pressing Tasks

### Output to SQL
- Create a connection and execute procedures from the pandas dataframe to sql. The function from the dataframe will be .to_sql, but requires a connection method. Just specifying an output name does not suffice as in the .to_csv function.
```TypeError: to_sql() missing 1 required positional argument: 'con'```



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

### Corruption
- Values that are 'bad' (i.e -99999, null, nan, -1E30)
- Push to random spots in column and whole DataFrame
- Set up extent of corruption (i.e harsh (70% of data), light (20% of data))



# Required Python Modules
Module       | Submodule(s) | as | Uses
------------ | ------------- | ------------- | -------------
**pandas**              | -                | pd          | DataFrames, indexing, plotting, downloading http url data, csv_reader()
**numpy**               | -                | np          | NaN values
**spacepy**             | pycdf            | -           |  Reading Common Data Format
**urllib**              | error            | -           | For HTTPError recognition
**random**              | -                | -           | Randomizer for random colors
**matplotlib**          | .pyplot, .mdates | plt, mdates | Plotting, subplots, date formatting
**datetime**            | -                | -           | Datetime indexing, datetime strings, datetime conversion from strings
**sys**                 | -                | -           | Exiting script
**wget**                | -                | -           | Downloading files online (.cdf, .csv, .ascii, .txt)
**os**                  | -                | -           | Remove files through script
**geopy.geocoders**     | Nominatim        | -           | Enables realtime verification of given latitudes and longitudes



# Running Scripts

### OMNI Space Weather ([omni_script_v2](https://github.com/byamashiro/Research_Projects/blob/master/Scripts/pandas_test_omni.py))




[//]: <> <img src="Plots/omni_test.png" width="600">




# Deprecated Scripts
Deprecated [scripts](https://github.com/byamashiro/Research_Projects/tree/master/Scripts/deprecated_scripts) are kept for reference. All scripts are working, but most do not incorporate online data fetching.
 

# Data
The data consists of mainly flux data from instruments on the ground, Earth orbit, and at the L1 Lagrange point. The data includes a sample from (2012 March), not normalized, and complete in intervals of about 30 seconds to a minute. Data values that were not accepted are denoted at extreme negative values around -9999. The specifics of each data set is commented in each header.

### Data Caveats
Corrupted data is labeled as -99999.0, and 0.0 flux is most probable to be corrupted as well. Corrupted data is changed using the pandas replace function to np.nan.

### Data Originals
GOES-13 Proton Flux  
GOES-15 Xray Flux  
ACE Magnetic Field Components  
ACE Solar Wind Parameters  
OULU Neutron Monitor Data  

### Sample Data


# Completed Tasks

# Resolved Errors

### Dynamic subplots and modifications to the Omni script (7/15/2017)
* **Resolution**: Set up a global variable to initialize a dynamic variable that would allow for slicing with a defined set. To make this work, the .axes slicing method was invoked, but required an overhaul on the plot function for each dataset (i.e. every plot function needed to be the same, with only the global index changing). Using the .axes slices allowed for subplots, but in turn, .plt functions did not edit all subplots. The .plt functions only edit the final added subplot, therefore changes must be added right after the plot function for each subplot using the .axes methods.
- Devise a way to plot selected datasets on subplots. The script runs with all data is loaded, but breaks with selections. Although the script is dynamic, there currently must be a static plot to host the first plot, and then subplots are appended to that "anchor" plot. Therefore, if the static anchor dataset is not chosen, the script cannot build on an empty canvas. The optimal solution seems to be unpacking different subplots (i.e. fig, (ax1, ax2, ...)). This solution requires that ax1, etc. must be literals and not strings, which removes options such as "for" loops with a list. An idea was to force a string to be a variable name, but this option should not be used if possible. A lambda function was also considered, but wildcard logic doesn't seem optimal for data frames while calling .index and columnized data.
- Minor tick gridlines for y-axis should be added with minorticks on. Add legends for each subplot and y-axis labels with units. but also reduce size of the legend and y-axis labels. Neutron monitor data seems to be cut off past the ~23 hour mark, include the rest of that data. Insert an "if" statement to deter plotting of neutron monitor data (long-term changes) and type III radio burst data (short-term changes) on the same canvas. 

