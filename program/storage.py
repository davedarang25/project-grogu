import csv


def save_student(
    studentID,
    name,
    section,
    eventName,
    eventTime,
    eventDate,
    status="Absent",
    filename="students.txt"
):
    """Append one student's details and chosen event to storage."""
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            studentID,
            name,
            section,
            eventName,
            eventTime,
            eventDate,
            status
        ])


def load_students(filename="students.txt"):
    """Load all student records from storage."""
    students = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                if len(row) == 7:
                    studentID, name, section, eventName, eventTime, eventDate, status = row

                elif len(row) == 6:
                    studentID, name, eventName, eventTime, eventDate, status = row
                    section = "Not set"

                else:
                    continue

                students.append(
                    (
                        studentID,
                        name,
                        section,
                        eventName,
                        eventTime,
                        eventDate,
                        status
                    )
                )

    except FileNotFoundError:
        pass

    return students


def save_all_students(participants, filename="students.txt"):
    """Rewrite all student records after attendance changes or undo."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for participant in participants:
            writer.writerow([
                participant.studentID,
                participant.name,
                participant.section,
                participant.eventName,
                participant.eventTime,
                participant.eventDate,
                participant.status
            ])


def list_students(filename="students.txt"):
    """Print all registered students and their chosen events."""
    students = load_students(filename)

    if not students:
        print("No students registered yet.")
        return

    print("\n=== Registered Students ===")

    for studentID, name, section, eventName, eventTime, eventDate, status in students:
        print(
            f"ID: {studentID} | "
            f"Name: {name} | "
            f"Section: {section} | "
            f"Event: {eventName} | "
            f"Date: {eventDate} | "
            f"Time: {eventTime} | "
            f"Status: {status}"
        )


def save_event(name, time, date, filename="event.txt"):
    """Save the latest event shown in the organizer summary."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, time, date])


def load_event(filename="event.txt"):
    """Load the latest event summary details."""
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            row = next(reader, None)

            if not row:
                return None

            if len(row) == 3:
                name, time, date = row

            elif len(row) > 3:
                name = row[0]
                time = row[1]
                date = ",".join(row[2:]).strip()

            else:
                return None

            return name, time, date

    except FileNotFoundError:
        pass

    return None


def save_event_slot(name, time, date, filename="event_slots.txt"):
    """Append one scheduled event slot to storage."""
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, time, date])


def load_event_slots(filename="event_slots.txt"):
    """Load all scheduled event slots."""
    event_slots = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                if len(row) == 3:
                    name, time, date = row

                elif len(row) > 3:
                    name = row[0]
                    time = row[1]
                    date = ",".join(row[2:]).strip()

                else:
                    continue

                event_slots.append({
                    "name": name,
                    "time": time,
                    "date": date
                })

    except FileNotFoundError:
        pass

    return event_slots


def save_all_event_slots(event_slots, filename="event_slots.txt"):
    """Rewrite all event slots after one event is deleted."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for slot in event_slots:
            writer.writerow([
                slot["name"],
                slot["time"],
                slot["date"]
            ])