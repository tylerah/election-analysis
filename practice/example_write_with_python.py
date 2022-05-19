# import csv module
import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a vairable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)

    

# Use the with statement to open the file as a text file
with open (file_to_save, "w") as txt_file:
    # write some data to the file
    line1 = "Counties in the Election\n"
    line2 = "------------------------\n"
    line3 = "Arapahoe\n"
    line4 = "Denver\n"
    line5 = "Jefferson"

    txt_file.writelines([line1, line2, line3, line4, line5])

txt_file.close()