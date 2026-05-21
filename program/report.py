# report.py
from registration import participants
from sorting import bubble_sort
from timeline import Timeline

timeline = Timeline()


def choose_sort_option(report_list):
    """Sort a report list using Bubble Sort."""
    print("\nSort by:")
    print("[1] Name")
    print("[2] ID")
    print("[3] Section")
    print("[4] Status")
    print("[5] Event")

    choice = input("Enter choice [1-5]: ").strip()

    if choice == "1":
        return bubble_sort(
            report_list,
            lambda participant: participant.name.lower(),
            ascending=True
        )

    elif choice == "2":
        return bubble_sort(
            report_list,
            lambda participant: participant.studentID.lower(),
            ascending=True
        )

    elif choice == "3":
        return bubble_sort(
            report_list,
            lambda participant: participant.section.lower(),
            ascending=True
        )

    elif choice == "4":
        return bubble_sort(
            report_list,
            lambda participant: participant.status.lower(),
            ascending=True
        )

    elif choice == "5":
        return bubble_sort(
            report_list,
            lambda participant: participant.eventName.lower(),
            ascending=True
        )

    else:
        print("Invalid choice. Showing unsorted list.")
        return report_list


def print_report(report_title, report_list):
    """Print the selected report."""
    print(f"\n=== {report_title} ===")

    if not report_list:
        print("No participants found.")
        return

    sorted_list = choose_sort_option(report_list)

    for participant in sorted_list:
        print(participant.viewDetails())


def generate_overall_report():
    """Generate report for all participants."""
    print_report("Overall Attendance Report", participants)


def generate_section_report():
    """Generate report filtered by section."""
    section = input("Enter section to report: ").strip()

    if not section:
        print("Section cannot be empty.")
        return

    section_list = [
        participant for participant in participants
        if participant.section.lower() == section.lower()
    ]

    print_report(f"Attendance Report for Section {section}", section_list)


def choose_event_for_report():
    """Let the user choose an event for event-based report."""
    event_slots = timeline.get_event_slots()

    if not event_slots:
        print("No events available.")
        return None

    print("\n=== Available Events ===")

    for number, slot in enumerate(event_slots, start=1):
        print(
            f"[{number}] {slot['name']} | "
            f"Date: {slot['date']} | "
            f"Time: {slot['time']}"
        )

    choice = input("Choose event number: ").strip()

    if not choice.isdigit():
        print("Invalid choice.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(event_slots):
        print("Invalid event selection.")
        return None

    return event_slots[index]


def generate_event_report():
    """Generate report filtered by selected event."""
    selected_event = choose_event_for_report()

    if selected_event is None:
        return

    event_list = [
        participant for participant in participants
        if participant.eventName == selected_event["name"]
        and participant.eventTime == selected_event["time"]
        and participant.eventDate == selected_event["date"]
    ]

    title = (
        f"Attendance Report for {selected_event['name']} "
        f"({selected_event['date']} | {selected_event['time']})"
    )

    print_report(title, event_list)


def generate_report():
    """Generate overall, section-based, or event-based report."""
    print("\n=== Generate Report ===")
    print("[1] Overall Report")
    print("[2] Report by Section")
    print("[3] Report by Event")
    print("[4] Return")

    choice = input("Enter choice [1-4]: ").strip()

    if choice == "1":
        generate_overall_report()

    elif choice == "2":
        generate_section_report()

    elif choice == "3":
        generate_event_report()

    elif choice == "4":
        print("Returning to main menu...")

    else:
        print("Invalid choice.")