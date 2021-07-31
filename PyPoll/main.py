# import csv and os
import csv
import os

#load files
load_file = os.path.join("PyPoll", "Resources", "election_data.csv")
output_file = os.path.join("PyPoll", "Analysis", "Text File")


vote_total = 0

candidateOptions = []
candidateVotes = {}

winningCandidate = ""
winningCount = 0 

# Read the CSV in
with open(load_file) as election_data:
  reader = csv.reader(election_data)

  header = next(reader)

  for row in reader:

    vote_total = vote_total + 1

    candidate_name = row[2]

    if candidate_name not in candidateOptions:
      candidateOptions.append(candidate_name)

      candidateVotes[candidate_name] = 0

    candidateVotes[candidate_name] = candidateVotes[candidate_name] + 1 

with open(output_file, "w") as txt_file:

  election_results = (
    f"\n\nElection Results\n"
    f"----------------------\n"
    f"Total Votes: {vote_total}\n"
    f"----------------------\n")
  print(election_results)  #end="")
  txt_file.write(election_results)


  for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    percentage_of_vote = float(votes) / float(vote_total) * 100

    if(votes > winningCount):
      winningCount = votes
      winningCandidate = candidate

    voter_output = f"{candidate}: {percentage_of_vote:.3f}% ({votes})\n"
    print(voter_output) #end="")
    txt_file.write(voter_output)

  winningCandidate_sum = (
    f"-----------------------\n"
    f"Winner: {winningCandidate}\n"
    f"-----------------------\n")
  print(winningCandidate_sum)
  txt_file.write(winningCandidate_sum)
