# Analysis of Election Data Utilizing Python
## Overview of Election Audit
### Purpose
The purpose of this project was to utilize a python script to provide an analysis of the results from a recent congressional election to the Colorado Board of Elections. Such an analysis has been performed using Excel in the past, however, the head of the Board of Elections believes that this process could be automated utilizing python. If a python script can be successfully used to provide an audit of the election data, then the board would like to modify this script in order to analyze all future elections held in the state. 
## Election Audit Results
### The Data
The data utilized for this audit was provided in a csv file that contained 3 pieces of data: the Ballot ID, the county to which the Ballot ID belonged, and the candidate for whom the vote was cast. 

The following data was extracted from this csv file utilizing a python script and was included in the final report:
1. The total number of votes cast in the election
2. The total number of votes cast in each county (Denver, Arapahoe, Jefferson)
3. The percentage of total votes contributed by each county (Denver, Arapahoe, Jefferson)
4. The total number of votes cast for each candidate
5. The percentage of total votes received by each candidate
6. The candidate who won the election based on the popular vote
### Election Audit Results
The results of the audit were as follows:
1. Total number of votes cast in the election: 369,711
2. Total number and percentage of votes cast in each county:
    * Denver: 306,055 (82.8%)
    * Jefferson: 38,855 (10.5%)
    * Arapahoe: 24,801 (6.7%)
3. The country with the largest turnout: Denver
4. The total number and percentage of votes cast for each candidate:
    * Diana DeGette: 272,892 (73.8%)
    * Charles Casper Stockham: 85,213 (23.0%)
    * Raymon Anthony Davis: 11,606 (3.1%)
5. The winner of the election: Diana DeGette with 272,892 total votes (73.8% of all votes)

Below is an example of how this data would appear in the command line / terminal after running the python script:
![example_terminal_output](https://user-images.githubusercontent.com/104606662/170365693-25b31615-2ca2-447b-9f05-81f1bd4917fe.png)

Below is an example of the text file that would be written by the python script:
![example_text_output](https://user-images.githubusercontent.com/104606662/170365956-3b314ace-ce6b-45d2-b2b3-81dd1d26918d.png)

## Election Audit Summary
### Potential Modifications
As the python script was proven to be successful, a variety of modifications could be made to provide a more thorough analysis in the future.

One potential modification would be to utilize the python script to further break down the data by demographics. This would require that the raw data include additional identifying information associated with each Ballot ID (such as age, race, and/or gender identity). The python script could then be utilized to determine the percentage of votes cast for any given candidate based on various demographic characteristics. This information may prove useful in determining voting patterns in a given demographic. 

A second potential modification that could prove useful would be to determine what percentage of the population actually cast a vote. This script determines what percentage of the votes cast were contributed by each county. However, if supplied with the total population data, the script coudl be modified to report what percentage of eligible voters actually cast a vote. This data could then be combined with the demographic data mentioned in the preceding paragraph to help the Board of Elections understand which sectors of the population are participating in the elections and which are not.
