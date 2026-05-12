# attendance.py
from logger import log_event
from registration import participants

def mark_attendance():
    studentID = input("Enter student ID to mark attendance: ").strip()
    found = False

    for participant in participants:
        if participant.studentID == studentID:
            participant.markPresent()
            log_event(f"Attendance marked: {participant.viewDetails()}")
            found = True
            break

    if not found:
        print("Participant not found.")
