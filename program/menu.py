# menu.py

def show_main_menu():
    print("\n" + "=" * 50)
    print("        EVENT ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("                 MAIN MENU")
    print("-" * 50)
    print("[1] Register Participant")
    print("[2] Mark Attendance")
    print("[3] Search Participant")
    print("[4] Undo Last Action")
    print("[5] Generate Report")
    print("[6] Exit")
    print("-" * 50)

    choice = input("Enter your choice [1-6]: ").strip()
    return choice