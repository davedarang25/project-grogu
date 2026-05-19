# organizer py
from program.event import Event

class Organizer:
    def __init__(self, name, organizer_id):
        self.name = name
        self.organizer_id = organizer_id
        self.events_managed = []

    def assign_event(self, event):
        self.events_managed.append(event)
        print(f"Organizer {self.name} is now managing event: {event.event_name}")
    
    def view_events(self):
        if not self.events_managed:
            print(f"Organizer {self.name} has no assigned events.")
        else:
            print(f"\nEvents managed by {self.name}:")
            for e in self.events_managed:
                print(f"- {e.event_name} on {e.date} at {e.venue}")

# Usage
if __name__ == "__main__":
    from event import Event

    # Organizer
    org = Organizer("Alice", "ORG26")

    # Create events
    event1 = Event("Tech Conference", "2024-09-15", "Convention Center")
    event2 = Event("Music Festival", "2024-10-20", "City Park")

    # View events
    org.view_events()