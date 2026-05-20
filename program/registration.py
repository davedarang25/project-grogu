# registration.py
from participant import Participant
from utils import validate_input
from logger import log_event
from storage import save_student, list_students
from timeline import Timeline

participants = []
timeline = Timeline()


def choose_event():
    """Let the student choose which event they will attend."""
    event_slots = timeline.get_event_slots()

    if not event_slots:
        print("No events are currently available for registration.")
        return None

    print("\n=== Available Events ===")
    for number, slot in enumerate(event_slots, start=1):
        print(
            f"[{number}] {slot['name']} | "
            f"Date: {slot['date']} | "
            f"Time: {slot['time']}"
        )

    choice = input("What event will you be attending? Enter number: ").strip()

    if not choice.isdigit():
        print("Invalid choice.")
        return None

    choice_index = int(choice) - 1

    if choice_index < 0 or choice_index >= len(event_slots):
        print("Invalid event selection.")
        return None

    return event_slots[choice_index]


def register_participant():
    name = input("Enter participant name: ").strip()
    studentID = input("Enter student ID: ").strip()

    if not validate_input(name, studentID, participants):
        print("Registration failed due to duplicate ID.")
        return

    selected_event = choose_event()

    if selected_event is None:
        print("Registration cancelled.")
        return

    new_participant = Participant(
        name,
        studentID,
        selected_event["name"],
        selected_event["time"],
        selected_event["date"]
    )

    participants.append(new_participant)

    save_student(
        studentID,
        name,
        selected_event["name"],
        selected_event["time"],
        selected_event["date"],
        new_participant.status
    )

    log_event(f"Registered participant: {new_participant.viewDetails()}")

    print("Registration successful.")

    list_students()
