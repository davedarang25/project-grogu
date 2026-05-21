from stack import Stack
from logger import log_event
from storage import save_all_students

undo_stack = Stack()


def undo_action():
    """Undo the latest registration or attendance action."""
    if undo_stack.isEmpty():
        print("No actions to undo.")
        return

    action_data = undo_stack.pop()
    action = action_data[0]

    from registration import participants

    if action == "register":
        participant = action_data[1]

        if participant in participants:
            participants.remove(participant)
            save_all_students(participants)

            print(f"Undo: Removed {participant.name} from registration.")
            log_event(f"Undo registration: {participant.viewDetails()}")
        else:
            print("Unable to undo registration. Student was not found.")

    elif action == "attendance":
        participant = action_data[1]
        previous_status = action_data[2]

        participant.status = previous_status
        save_all_students(participants)

        print(f"Undo: Restored {participant.name}'s attendance to {previous_status}.")
        log_event(f"Undo attendance: {participant.viewDetails()}")

    else:
        print("Unknown action. Nothing was undone.")