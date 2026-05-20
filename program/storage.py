# storage py

def save_student(
    studentID,
    name,
    eventName,
    eventTime,
    eventDate,
    status="Absent",
    filename="students.txt"
):
    """Save student details and chosen event to a file."""
    with open(filename, "a") as file:
        file.write(
            f"{studentID},{name},{eventName},"
            f"{eventTime},{eventDate},{status}\n"
        )

def load_students(filename="students.txt"):
    """Load student details from file."""
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 6:
                    studentID, name, eventName, eventTime, eventDate, status = data
                    students.append(
                        (studentID, name, eventName, eventTime, eventDate, status)
                    )

    except FileNotFoundError:
        pass

    return students

def list_students(filename="students.txt"):
    """Print a list of all registered students and their chosen events."""
    students = load_students(filename)

    if not students:
        print("No students registered yet.")
        return

    print("\n=== Registered Students ===")

    for studentID, name, eventName, eventTime, eventDate, status in students:
        print(
            f"ID: {studentID} | "
            f"Name: {name} | "
            f"Event: {eventName} | "
            f"Date: {eventDate} | "
            f"Time: {eventTime} | "
            f"Status: {status}"
        )

def save_event(name, time, date, filename="event.txt"):
    """Save the current event details to a file."""
    with open(filename, "w") as file:
        file.write(f"{name},{time},{date}\n")


def load_event(filename="event.txt"):
    """Load the saved event details from a file."""
    try:
        with open(filename, "r") as file:
            line = file.readline().strip()

            if line:
                name, time, date = line.split(",")
                return name, time, date

    except FileNotFoundError:
        pass

    return None
def save_event_slot(name, time, date, filename="event_slots.txt"):
    """Save an event slot to a file."""
    with open(filename, "a") as file:
        file.write(f"{name},{time},{date}\n")


def load_event_slots(filename="event_slots.txt"):
    """Load all saved event slots from a file."""
    event_slots = []

    try:
        with open(filename, "r") as file:
            for line in file:
                name, time, date = line.strip().split(",")

                event_slots.append({
                    "name": name,
                    "time": time,
                    "date": date
                })

    except FileNotFoundError:
        pass

    return event_slots