# menu.py
from utils import clear_screen

def show_main_menu():
    clear_screen()
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

def show_organizer_menu():
    print("\n" + "=" * 50)
    print("                 ORGANIZER MENU")
    print("=" * 50)
    print("[1] Set Event Details")
    print("[2] View Attendee List")
    print("[3] View Event Summary")
    print("[4] Complete/Delete Finished Event")
    print("[5] Return to Main Menu")
    print("-" * 50)

    choice = input("Enter your choice [1-5]: ").strip()
    
    return choice

def show_role_menu():
    clear_screen()
    print("\n" + "=" * 50)
    print("        EVENT ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("              SELECT USER TYPE")
    print("-" * 50)
    print("[1] Organizer")
    print("[2] Student")
    print("[3] Exit")
    print("-" * 50)

    choice = input("Enter your choice [1-3]: ").strip()
    clear_screen()
    return choice