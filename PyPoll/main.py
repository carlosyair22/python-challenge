import csv
import os

#variables that will be used to gather the statistics
votes=0
candidateNames=["Khan", "Correy", "Li", "O'Tooley"]
candidateVotes=[0,0,0,0]

file=os.path.join("election_data.csv")
with open(file,"r") as election_data:
    electionReader=csv.reader(election_data,delimiter=",")
    # Remove header line
    header=next(electionReader)
    # for each row, sum the vote corresponding to each one of the four candidates in candiateVotes list
    for rows in electionReader:
        n=candidateNames.index(rows[2])
        candidateVotes[n]+=1
        votes+=1

#Determine which candidate won the election comparing the votes
maxvotes=0
for votescount in candidateVotes:
    if votescount>maxvotes:
        maxvotes=votescount
        n=candidateVotes.index(votescount)
        winner=candidateNames[n]

#Print the results in the terminal and write them in the results .txt file
openning=(f'''Election Results
--------------------------
Total Votes: {votes}
--------------------------''')
print(openning)
f=open("election_results.txt","w+")
f.write(openning)
for n in range(4):
    print(f"{candidateNames[n]}: {round(candidateVotes[n]*100/votes,1)}% ({candidateVotes[n]})")
    f.writelines(f"\n{candidateNames[n]}: {round(candidateVotes[n]*100/votes,1)}% ({candidateVotes[n]})")
closing=(f'''\n--------------------------
Winner: {winner}
--------------------------''')
print(closing)
f.writelines(closing)