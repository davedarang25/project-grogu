# storage py

def save_student(studentID, name, status="Absent", filename="students.txt"):
    """Save student details to a file."""
    with open(filename, "a") as file:
        file.write(f"{studentID},{name},{status}\n")

def load_students(filename="students.txt"):
    """Load student details from file"""
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                studentID, name, status = line.strip().split(",")
                students.append((studentID, name, status))
    except FileNotFoundError:
        pass
    return students

def list_students(filename="students.txt"):
    """Print a list of all student IDs and names."""
    students = load_students(filename)
    if not students:
        print("No students registered yet.")
        return
    print("\n=== Registered Students ===")
    for studentID, name, status in students:
        print(f"ID: {studentID} | Name: {name} | Status: {status}")