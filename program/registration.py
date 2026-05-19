# registration.py
from participant import Participant
from utils import validate_input
from logger import log_event
from storage import save_student, list_students

participants = []


def make_full_name():
    surname = input("Enter surname: ").strip()
    first_name = input("Enter first name: ").strip()
    middle_initial = input("Enter middle initial: ").strip()

    if middle_initial:
        middle_initial = middle_initial.replace(".", "")
        middle_initial = middle_initial[0].upper() + "."
        name = f"{surname}, {first_name} {middle_initial}"
    else:
        name = f"{surname}, {first_name}"

    return name


def generate_guest_number():
    guest_count = 1

    while True:
        guest_number = f"GUEST-{guest_count:03d}"

        duplicate = False

        for participant in participants:
            if participant.studentID == guest_number:
                duplicate = True
                break

        if not duplicate:
            return guest_number

        guest_count += 1


def register_student():
    print("\n=== Student Registration ===")

    name = make_full_name()
    studentID = input("Enter student ID: ").strip()

    if validate_input(name, studentID, participants):
        new_participant = Participant(name, studentID)
        participants.append(new_participant)

        save_student(studentID, name, new_participant.status, "Student")

        log_event(f"Registered student: {new_participant.viewDetails()}")

        print("Student registration successful.")
        list_students()

    else:
        print("Registration failed due to duplicate ID.")


def register_guest():
    print("\n=== Guest Registration ===")

    name = make_full_name()
    guest_number = generate_guest_number()

    print(f"Guest number assigned: {guest_number}")

    if validate_input(name, guest_number, participants):
        new_participant = Participant(name, guest_number)
        participants.append(new_participant)

        save_student(guest_number, name, new_participant.status, "Guest")

        log_event(f"Registered guest: {new_participant.viewDetails()}")

        print("Guest registration successful.")
        list_students()

    else:
        print("Guest registration failed due to duplicate guest number.")


def register_participant():
    while True:
        print("\n=== Register Participant ===")
        print("1. Student")
        print("2. Guest")
        print("3. Back")

        choice = input("Choose participant type: ").strip()

        if choice == "1":
            register_student()

        elif choice == "2":
            register_guest()

        elif choice == "3":
            return

        else:
            print("Invalid choice. Please try again.")