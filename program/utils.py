# utils.py

def validate_input(name, studentID, participants):
    """Check for duplicate participant IDs before registration."""
    for participant in participants:
        if participant.studentID == studentID:
            print("Duplicate ID found. Registration failed.")
            return False
    return True

def format_text(text):
    """Format text for consistent display."""
    return f"*** {text} ***"

def handle_error(message):
    """Display error messages consistently."""
    print(f"[ERROR] {message}")
