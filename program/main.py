# main.py
import sys
from menu import show_main_menu
from registration import register_participant
from attendance import mark_attendance
from search import search_participant
from undo import undo_action
from report import generate_report

def main():
    print("=== Welcome to the Campus Event Registration and Attendance System ===")

    while True:
        choice = show_main_menu()

        if choice == "1":  # Register
            register_participant()

        elif choice == "2":  # Attendance
            mark_attendance()

        elif choice == "3":  # Search
            search_participant()

        elif choice == "4":  # Undo
            undo_action()

        elif choice == "5":  # Report
            generate_report()

        elif choice == "6":  # Exit
            confirm = input("Exit System? (y/n): ").strip().lower()
            if confirm == "y":
                print("Thank you for using the system!")
                sys.exit(0)
            else:
                continue

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()