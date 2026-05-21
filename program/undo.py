# undo.py
from stack import Stack
from registration import participants
from logger import log_event

undo_stack = Stack()

def undo_action():
    if undo_stack.isEmpty():
        print("No actions to undo.")
        return

    action, participant = undo_stack.pop()
    if action == "register":
        participants.remove(participant)
        print(f"Undo: Removed {participant.name} from registration.")
        log_event(f"Undo registration: {participant.viewDetails()}")
    elif action == "attendance":
        participant.markAbsent()
        print(f"Undo: Reset {participant.name}'s attendance to Absent.")
        log_event(f"Undo attendance: {participant.viewDetails()}")
