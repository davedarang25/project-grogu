from registration import participants
from timeline import Timeline
from logger import log_event
from menu import show_organizer_menu
from sorting import bubble_sort
from storage import save_event, load_event
from event import Event

saved_event = load_event()

if saved_event:
    name, time, date = saved_event
    current_event = Event(name, time, date)
else:
    current_event = Event()

timeline = Timeline()

# Stores the current event details entered by the organizer.

def set_event_details():
    """Allow the organizer to enter the event name, time, and date together."""
    name = input("Enter event name: ").strip()
    time = input("Enter event time range, e.g. 9:00 AM - 11:00 AM: ").strip()
    date = input("Enter event date: ").strip()

    if not name or not time or not date:
        print("Event name, time, and date cannot be empty.")
        return

    if timeline.is_slot_taken(date, time):
        print("Slot taken. Another event is already scheduled for that date and time.")
        return

    current_event.setDetails(name, time, date)

    timeline.add_event_slot(name, time, date)
    save_event(name, time, date)

    log_event(f"Event details set: Name={name}, Time={time}, Date={date}")
    print("Event details saved successfully.")


def view_attendee_list():
    """Display the attendee list with sorting options."""
    print("\n=== Attendee List ===")

    if not participants:
        print("No attendees registered yet.")
        return

    print("[1] Sort by Name - Ascending")
    print("[2] Sort by Name - Descending")
    print("[3] Sort by Time - Preparation")
    print("[4] Sort by Section - Preparation")
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
        print("Sorting by time is still in preparation.")
        return

    elif choice == "4":
        print("Sorting by section is still in preparation.")
        return

    elif choice == "5":
        print("Returning to organizer menu...")
        return

    else:
        print("Invalid choice. Please try again.")
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

        elif choice == "2":
            view_attendee_list()

        elif choice == "3":
            view_event_summary()

        elif choice == "4":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")