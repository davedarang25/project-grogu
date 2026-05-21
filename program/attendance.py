from logger import log_event
from registration import participants
from storage import save_all_students
from undo import undo_stack


def mark_attendance():
    """Mark one student as present and save the change."""
    studentID = input("Enter student ID to mark attendance: ").strip()

    for participant in participants:
        if participant.studentID == studentID:
            if participant.status == "Present":
                print(f"{participant.name} is already marked as Present.")
                return

            previous_status = participant.status
            participant.markPresent()

            undo_stack.push(("attendance", participant, previous_status))
            save_all_students(participants)

            log_event(f"Attendance marked: {participant.viewDetails()}")
            return

    print("Student not found.")