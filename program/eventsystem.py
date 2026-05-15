# eventsystem.py

from participant import Participant
from queue import Queue
from stack import Stack

class EventSystem:
    def __init__(self):
        self.eventList = []          # Stores event names/details
        self.participantList = []    # Stores Participant objects
        self.queue = Queue()         # Queue for registrations
        self.stack = Stack()         # Stack for undo actions

    def registerParticipant(self, name: str, studentID: str):
        """Register a new participant and add to queue."""
        participant = Participant(name, studentID)
        self.participantList.append(participant)
        self.queue.enqueue(participant)
        self.stack.push(("register", participant))
        print(f"Registered: {participant.viewDetails()}")

    def markAttendance(self, studentID: str, status: str = "Present"):
        """Mark attendance for a participant by ID."""
        for participant in self.participantList:
            if participant.studentID == studentID:
                participant.status = status
                self.stack.push(("attendance", participant))
                print(f"Attendance updated: {participant.viewDetails()}")
                return
        print("Participant not found.")

    def generateReport(self, sortKey: str = "name"):
        """Generate a sorted report of participants."""
        if sortKey == "name":
            sorted_list = sorted(self.participantList, key=lambda p: p.name)
        elif sortKey == "id":
            sorted_list = sorted(self.participantList, key=lambda p: p.studentID)
        elif sortKey == "status":
            sorted_list = sorted(self.participantList, key=lambda p: p.status)
        else:
            sorted_list = self.participantList

        print("\n=== Attendance Report ===")
        for participant in sorted_list:
            print(participant.viewDetails())

    def undoAction(self):
        """Undo the most recent action using the stack."""
        if self.stack.isEmpty():
            print("No actions to undo.")
            return

        action, participant = self.stack.pop()
        if action == "register":
            self.participantList.remove(participant)
            print(f"Undo: Removed {participant.name} from registration.")
        elif action == "attendance":
            participant.status = "Absent"
            print(f"Undo: Reset {participant.name}'s attendance to Absent.")