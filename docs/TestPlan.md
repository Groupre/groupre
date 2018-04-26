# groupre Test Plan

## Test Platforms

### Web

Testing will be of the Python (Flask)/JavaScript product, to be tested on Carolina CloudApps or hosted locally on developer machines.

### Command-Line

Testing will be of the core Python back-end module through direct calling of the Python module.

## Test Cases

Test cases are expected to yield information confirming successful processing of input data in accordance with program parameters. Failing that, testing is expected to yield errors related to either the algorithm’s processing of the data, or data input errors. 
Specific issues that will be tested for include, but are not limited to the following:

* Students who are able to ask for outlandish amounts of preferences for Chair attributes that have no overlap (read: chairs that fulfill all criteria) are hard to account for. It is expected that a given Student will not be able to make so many selections of preferences to where this scenario is realistic, however.
* Not all csv files follow the same standard. Testing for csv input errors will address those potential issues.
* The GUI will require extensive testing to detect and prevent crashes.
* Extreme edge cases have been added to the testing list.

Test csv files can be found in the project repository within the test directory. The hosted CloudApps site also has test cases available for download.