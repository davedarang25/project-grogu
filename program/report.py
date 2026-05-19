# report.py
from registration import participants

def generate_report():
    print("\n=== Generate Report ===")
    print("Sort by: 1. Name  2. ID  3. Status")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_list = sorted(participants, key=lambda p: p.name)
    elif choice == "2":
        sorted_list = sorted(participants, key=lambda p: p.studentID)
    elif choice == "3":
        sorted_list = sorted(participants, key=lambda p: p.status)
    else:
        print("Invalid choice. Showing unsorted list.")
        sorted_list = participants

    print("\n=== Attendance Report ===")
    for participant in sorted_list:
        print(participant.viewDetails())
