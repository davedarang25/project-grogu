# storage.py

def save_student(studentID, name, status, participant_type="Student", filename="students.txt"):
    with open(filename, "a") as file:
        file.write(f"{name}|{participant_type}|{studentID}|{status}\n")


def load_students(filename="students.txt"):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                # New format:
                # Name | Type | ID Number | Status
                if "|" in line:
                    parts = line.split("|")

                    if len(parts) == 4:
                        name = parts[0].strip()
                        participant_type = parts[1].strip()
                        studentID = parts[2].strip()
                        status = parts[3].strip()

                        students.append({
                            "name": name,
                            "type": participant_type,
                            "studentID": studentID,
                            "status": status
                        })

                # Old format support:
                # ID,Name,Status
                else:
                    parts = line.split(",")

                    studentID = parts[0].strip()
                    status = parts[-1].strip()
                    name = ",".join(parts[1:-1]).strip()

                    if studentID.startswith("GUEST"):
                        participant_type = "Guest"
                    else:
                        participant_type = "Student"

                    students.append({
                        "name": name,
                        "type": participant_type,
                        "studentID": studentID,
                        "status": status
                    })

    except FileNotFoundError:
        return []

    return students


def list_students(filename="students.txt"):
    students = load_students(filename)

    print("\n=== Participant Records ===")

    if not students:
        print("No records found.")
        return

    print(f"{'Name':<30} | {'Type':<10} | {'ID Number':<15} | {'Status':<10}")
    print("-" * 75)

    for student in students:
        print(
            f"{student['name']:<30} | "
            f"{student['type']:<10} | "
            f"{student['studentID']:<15} | "
            f"{student['status']:<10}"
        )