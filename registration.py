# registration.py
from participant import Participant
from utils import validate_input
from logger import log_event
from storage import save_student, list_students

participants = []

def register_participant():
    name = input("Enter participant name: ").strip()
    studentID = input("Enter student ID: ").strip()

    if validate_input(name, studentID, participants):
        new_participant = Participant(name, studentID)
        participants.append(new_participant)

        # Save to student records file
        save_student(studentID, name, new_participant.status)

        # Log system event
        log_event(f"Registered participant: {new_participant.viewDetails()}")

        print("Registration successful.")

        # Show updated student list
        list_students()

    else:
        print("Registration failed due to duplicate ID.")
