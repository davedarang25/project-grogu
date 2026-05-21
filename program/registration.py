from participant import Participant
from utils import validate_input
from logger import log_event
from storage import save_student, list_students, load_students
from timeline import Timeline
from queue import Queue
from undo import undo_stack

participants = []
registration_queue = Queue()
timeline = Timeline()


def load_saved_participants():
    """Load saved student records into the in-memory participant list."""
    saved_students = load_students()

    for studentID, name, section, eventName, eventTime, eventDate, status in saved_students:
        participant = Participant(
            name,
            studentID,
            section,
            eventName,
            eventTime,
            eventDate,
            status
        )
        participants.append(participant)


load_saved_participants()


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
    """Register a student and record the event they will attend."""
    name = input("Enter student name: ").strip()
    studentID = input("Enter student ID: ").strip()
    section = input("Enter section: ").strip()

    if not name or not studentID or not section:
        print("Student name, student ID, and section cannot be empty.")
        return

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
        section,
        selected_event["name"],
        selected_event["time"],
        selected_event["date"]
    )

    participants.append(new_participant)
    registration_queue.enqueue(new_participant)
    undo_stack.push(("register", new_participant))

    save_student(
        studentID,
        name,
        section,
        selected_event["name"],
        selected_event["time"],
        selected_event["date"],
        new_participant.status
    )

    log_event(f"Registered student: {new_participant.viewDetails()}")

    print("Registration successful.")
    list_students()