# menu.py

def show_main_menu():
    print("\n=== Main Menu ===")
    print("1. Register Participant")
    print("2. Mark Attendance")
    print("3. Search Participant")
    print("4. Undo Last Action")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()
    return choice
