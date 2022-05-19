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

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Creat dictionary to link candidates with votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    ## to see if the headers were correctly removed, use the following: print(headers)

    #print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        # print the cadidate name from each row
        candidate_name = row[2]

        # add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
    
    for candidate_name in candidate_votes:
        # retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calcualte the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # determine winning vote count and candidate
        # determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    
    print(winning_candidate_summary)



## print information
print(f"Total Votes Cast: " + str(total_votes))
# print items in candidate_options list without the brackets
print("Candidates: " + ', '.join(str(x) for x in candidate_options))

    




# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote