# search.py
from registration import participants

def search_participant():
    query = input("Enter participant ID to search: ").strip()
    for participant in participants:
        if participant.studentID == query:
            print("Participant found:")
            print(participant.viewDetails())
            return
    print("Participant not found.")
