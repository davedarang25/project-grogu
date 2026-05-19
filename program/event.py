# event.py
class Event:
    def __init__(self, event_name, date, venue):
        self.event_name = event_name
        self.date = date
        self.venue = venue
        self.participants = []   # list of Participant objects

    def add_participant(self, participant):
        self.participants.append(participant)
        print(f"Participant {participant.name} registered for {self.event_name}.")

    def list_participants(self):
        if not self.participants:
            print(f"No participants registered for {self.event_name}.")
        else:
            print(f"\nParticipants for {self.event_name}:")
            for p in self.participants:
                print(f"- {p.name} (ID: {p.student_id})")

    def __str__(self):
        return f"{self.event_name} on {self.date} at {self.venue}"

    def details(self):
        return {
            "name": self.event_name,
            "date": self.date,
            "venue": self.venue,
            "participants": [p.name for p in self.participants]
        }
