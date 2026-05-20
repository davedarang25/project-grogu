from registration import participants
from sorting import bubble_sort


def generate_report():
    """Generate an attendance report using the custom Bubble Sort function."""
    print("\n=== Generate Report ===")
    print("Sort by: 1. Name  2. ID  3. Status")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.name.lower(),
            ascending=True
        )

    elif choice == "2":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.studentID.lower(),
            ascending=True
        )

    elif choice == "3":
        sorted_list = bubble_sort(
            participants,
            lambda participant: participant.status.lower(),
            ascending=True
        )

    else:
        print("Invalid choice. Showing unsorted list.")
        sorted_list = participants

    print("\n=== Attendance Report ===")

    if not sorted_list:
        print("No participants registered yet.")
        return

    for participant in sorted_list:
        print(participant.viewDetails())