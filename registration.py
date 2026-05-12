# registration.py
from participant import Participant
from utils import validate_input
from logger import log_event

participants = []  # shared list of participants

def register_participant():
    name = input("Enter participant name: ").strip()
    studentID = input("Enter student ID: ").strip()

    if validate_input(name, studentID, participants):
        new_participant = Participant(name, studentID)
        participants.append(new_participant)
        log_event(f"Registered participant: {new_participant.viewDetails()}")
        print("Registration successful.")
    else:
        print("Registration failed due to duplicate ID.")
