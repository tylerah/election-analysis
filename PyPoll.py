# The data we need to retrive
# path = resources/election_results.csv

# print date & time the code was executed
import datetime as dt
now = dt.datetime.now()

print("The time right now is ", now)

# import csv module
import csv
import os

# Assign variables for loading and saving file
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)




# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote