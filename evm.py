# ============================================
# Electronic Voting Machine System
# Author: Bhanuprasad Unnam
# ============================================

import pandas as pd

# Sample voter database
voters = pd.DataFrame({
    "voter_id": [101, 102, 103],
    "name": ["Ravi", "Suresh", "Priya"],
    "face_id": ["face101", "face102", "face103"],
    "has_voted": [0, 0, 0]
})

# Sample vote database
votes = pd.DataFrame({
    "candidate": ["Party A", "Party B", "Party C"],
    "votes": [0, 0, 0]
})

print("===================================")
print(" ELECTRONIC VOTING MACHINE SYSTEM ")
print("===================================\n")

# Test values instead of input()
voter_id = "101"
entered_face_id = "face101"
vote_choice = "1"

# Check voter exists
if voter_id in voters["voter_id"].astype(str).values:

    voter = voters[voters["voter_id"].astype(str) == voter_id]

    if voter.iloc[0]["has_voted"] == 1:

        print("You have already voted.")

    else:

        print("Face Verification Started...\n")

        actual_face_id = voter.iloc[0]["face_id"]

        if entered_face_id == actual_face_id:

            print("Face Verification Successful")
            print("Welcome,", voter.iloc[0]["name"])

            print("\nCandidates")
            print("1. Party A")
            print("2. Party B")
            print("3. Party C")

            if vote_choice == "1":

                votes.loc[0, "votes"] += 1
                selected_candidate = "Party A"

            elif vote_choice == "2":

                votes.loc[1, "votes"] += 1
                selected_candidate = "Party B"

            elif vote_choice == "3":

                votes.loc[2, "votes"] += 1
                selected_candidate = "Party C"

            else:

                print("Invalid Vote")
                exit()

            voters.loc[
                voters["voter_id"].astype(str) == voter_id,
                "has_voted"
            ] = 1

            print("\nVote Submitted Successfully")
            print("You voted for:", selected_candidate)

        else:

            print("Face Verification Failed")

else:

    print("Invalid Voter ID")

print("\nCurrent Results:\n")
print(votes)