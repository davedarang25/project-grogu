# participant.py

class Participant:
    def __init__(
        self,
        name: str,
        studentID: str,
        eventName: str = "Not selected",
        eventTime: str = "Not set",
        eventDate: str = "Not set",
        status: str = "Absent"
    ):
        self.name = name
        self.studentID = studentID
        self.eventName = eventName
        self.eventTime = eventTime
        self.eventDate = eventDate
        self.status = status

    def updateDetails(self, name: str = None, studentID: str = None):
        """Update participant details such as name or student ID."""
        if name:
            self.name = name
        if studentID:
            self.studentID = studentID
        print(f"Details updated: {self.viewDetails()}")

    def viewDetails(self) -> str:
        """Return participant details as a formatted string."""
        return (
            f"Name: {self.name}, "
            f"ID: {self.studentID}, "
            f"Event: {self.eventName}, "
            f"Date: {self.eventDate}, "
            f"Time: {self.eventTime}, "
            f"Status: {self.status}"
        )

    def markPresent(self):
        """Mark participant as present."""
        self.status = "Present"
        print(f"{self.name} has been marked as Present.")

    def markAbsent(self):
        """Mark participant as absent."""
        self.status = "Absent"
        print(f"{self.name} has been marked as Absent.")