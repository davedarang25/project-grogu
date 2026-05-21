# utils.py
import os

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
def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")
def pause_screen():
    """Pause the screen so the user can read the output."""
    input("\nPress Enter to continue...")