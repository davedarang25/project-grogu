from registration import participants
from timeline import Timeline
from logger import log_event
from menu import show_organizer_menu
from sorting import bubble_sort
from storage import save_event, load_event
from event import Event
from utils import pause_screen

saved_event = load_event()

if saved_event:
    name, time, date = saved_event
    current_event = Event(name, time, date)
else:
    current_event = Event()

timeline = Timeline()

# Stores the current event details entered by the organizer.

def set_event_details():
    """Allow the organizer to enter the event name, time range, and date together."""
    name = input("Enter event name: ").strip()
    time = input("Enter event time range, e.g. 9:00 AM - 11:00 AM: ").strip()
    date = input("Enter event date: ").strip()

    if not name or not time or not date:
        print("Event name, time, and date cannot be empty.")
        return

    added, message = timeline.add_event_slot(name, time, date)

    if not added:
        print(message)
        return

    current_event.setDetails(name, time, date)
    save_event(name, time, date)

    log_event(f"Event details set: Name={name}, Time={time}, Date={date}")
    print(message)

def event_matches_participant(participant, event_slot):
    """Check if a participant belongs to a selected event."""
    same_name = participant.eventName == event_slot["name"]
    same_time = participant.eventTime == event_slot["time"]
    same_date = participant.eventDate == event_slot["date"]

    return same_name and same_time and same_date


def choose_event_slot():
    """Let the organizer choose an event slot."""
    event_slots = timeline.get_event_slots()

    if not event_slots:
        print("No event slots available.")
        return None

    print("\n=== Event Slots ===")

    for number, slot in enumerate(event_slots, start=1):
        print(
            f"[{number}] {slot['name']} | "
            f"Date: {slot['date']} | "
            f"Time: {slot['time']}"
        )

    choice = input("Select event number: ").strip()

    if not choice.isdigit():
        print("Invalid choice.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(event_slots):
        print("Invalid event selection.")
        return None

    return event_slots[index]


def print_event_attendance(event_slot):
    """Print attendance record for a selected event."""
    event_attendees = []

    for participant in participants:
        if event_matches_participant(participant, event_slot):
            event_attendees.append(participant)

    print("\n=== Event Attendance ===")
    print(f"Event: {event_slot['name']}")
    print(f"Date : {event_slot['date']}")
    print(f"Time : {event_slot['time']}")
    print("-" * 50)

    if not event_attendees:
        print("No attendees registered for this event.")
        return

    present_count = 0
    absent_count = 0

    for number, participant in enumerate(event_attendees, start=1):
        print(f"{number}. {participant.viewDetails()}")

        if participant.status.lower() == "present":
            present_count += 1
        else:
            absent_count += 1

    print("-" * 50)
    print(f"Total Attendees : {len(event_attendees)}")
    print(f"Present         : {present_count}")
    print(f"Absent          : {absent_count}")


def delete_finished_event():
    """Print attendance, then delete a finished event slot."""
    selected_event = choose_event_slot()

    if selected_event is None:
        return

    print_event_attendance(selected_event)

    confirm = input("\nDelete this finished event? (y/n): ").strip().lower()

    if confirm != "y":
        print("Event deletion cancelled.")
        return

    deleted = timeline.delete_event_slot(selected_event)

    if deleted:
        global current_event

        if (
            current_event.name == selected_event["name"]
            and current_event.time == selected_event["time"]
            and current_event.date == selected_event["date"]
        ):
            remaining_events = timeline.get_event_slots()

            if remaining_events:
                latest_event = remaining_events[-1]
                current_event.setDetails(
                    latest_event["name"],
                    latest_event["time"],
                    latest_event["date"]
                )
                save_event(
                    latest_event["name"],
                    latest_event["time"],
                    latest_event["date"]
                )
            else:
                current_event.setDetails("Not set", "Not set", "Not set")
                save_event("Not set", "Not set", "Not set")

        log_event(
            f"Deleted finished event: "
            f"{selected_event['name']} | "
            f"{selected_event['date']} | "
            f"{selected_event['time']}"
        )

        print("Finished event deleted successfully.")
    else:
        print("Event was not found.")


def view_attendee_list():
    """Display the attendee list with sorting and status filter options."""
    print("\n=== Attendee List ===")

    if not participants:
        print("No attendees registered yet.")
        return

    print("[1] Sort by Name - Ascending")
    print("[2] Sort by Name - Descending")
    print("[3] Filter by Status - Present or Absent")
    print("[4] Sort by Section ")
    print("[5] Return")

    choice = input("Enter your choice [1-5]: ").strip()

    if choice == "1":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.name.lower(),
            ascending=True
        )
        print("\n=== Attendee List: Name Ascending ===")

    elif choice == "2":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.name.lower(),
            ascending=False
        )
        print("\n=== Attendee List: Name Descending ===")

    elif choice == "3":
        print("\n[1] Present")
        print("[2] Absent")

        status_choice = input("Choose status to view [1-2]: ").strip()

        if status_choice == "1":
            sorted_list = [
                participant for participant in participants
                if participant.status.lower() == "present"
            ]
            print("\n=== Attendee List: Present ===")

        elif status_choice == "2":
            sorted_list = [
                participant for participant in participants
                if participant.status.lower() == "absent"
            ]
            print("\n=== Attendee List: Absent ===")

        else:
            print("Invalid status choice.")
            return

        sorted_list = bubble_sort(
            sorted_list,
            lambda participant: participant.name.lower(),
            ascending=True
        )

    elif choice == "4":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.section.lower(),
            ascending=True
        )
        print("\n=== Attendee List: Section Ascending ===")

    elif choice == "5":
        print("Returning to organizer menu...")
        return

    else:
        print("Invalid choice. Please try again.")
        return

    if not sorted_list:
        print("No attendees found for this option.")
        return

    for number, participant in enumerate(sorted_list, start=1):
        print(f"{number}. {participant.viewDetails()}")


def view_event_summary():
    """Display the current event details and attendee count."""
    print("\n=== Event Summary ===")
    print(current_event.viewDetails())
    print(f"Attendees  : {len(participants)} registered")


def organizer_menu():
    """Handle organizer menu actions."""
    while True:
        choice = show_organizer_menu()

        if choice == "1":
            set_event_details()
            pause_screen()

        elif choice == "2":
            view_attendee_list()
            pause_screen()

        elif choice == "3":
            view_event_summary()
            pause_screen()

        elif choice == "4":
            delete_finished_event()
            pause_screen()

        elif choice == "5":
            print("Returning to user selection...")
            break

        else:
            print("Invalid choice. Please try again.")