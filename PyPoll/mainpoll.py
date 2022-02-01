import csv
import os
import pathlib


csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "election_data.csv")
#list of variables
total_votes = 0 
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
max_votes = 0
winner = ""

#  Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    for row in csv_reader:
        #row is a new variable created here.
        # total_votes = total_votes + 1 , shortcut
        total_votes += 1       
# this part goes through each row and adds all the votes for each candiate "khan_votes = Khan_votes + 1" then adds to Khan_votes varibale. 
        if row[2] == "Khan":                
            Khan_votes += 1                 
        elif row[2] == "Correy":
            Correy_votes += 1   
        elif row[2] == "Li":
            Li_votes += 1 
        elif row[2] == "O'Tooley":
            OTooley_votes += 1 
            #Creates dictionary
    candidates_dict = {"Khan": Khan_votes,       
                    "Correy": Correy_votes,                                     
                    "Li": Li_votes,
                    "O'Tooley": OTooley_votes
                    }
    for candidate, votes in candidates_dict.items(): 
        if votes > max_votes:
            max_votes = votes
            winner = candidate               

#output
print(f"Election Results")
print(f"-"*28)
print(f"Total Votes: {total_votes}")
print(f"-"*28)
print(f"Khan: {(Khan_votes / total_votes) * 100:.3f}% ({Khan_votes})")
print(f"Correy: {(Correy_votes / total_votes) * 100:.3f}% ({Correy_votes}) ")
print(f"Li: {(Li_votes / total_votes) * 100:.3f}%({Li_votes})")
print(f"O'Tooley:{(OTooley_votes / total_votes) * 100:.3f}% ({OTooley_votes})  ")
print(f"-"*28)
print(f"Winner: {winner}")
print(f"-"*28)

f = open("Pypolldata.txt",'w')
f.write("Election Results\n")
f.write(f"-28")
f.write("\n")
f.write(f"Khan: {Khan_votes}\n")
f.write(f"Correy : {Correy_votes}")
f.write(f"Li: {Li_votes}")
f.write(f"O'Tooley: {OTooley_votes}")
f.write(f"-28")
f.write(f"Winner: {winner}")
f.write(f"-28")
f.write(f"-"*28)
f.close()


