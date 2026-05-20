from datetime import datetime
from storage import save_event_slot, load_event_slots


class Timeline:
    def __init__(self):
        self.event_slots = load_event_slots()

    def convert_time(self, time_text):
        """Convert time text like '9:00 AM' into a comparable time value."""
        return datetime.strptime(time_text.strip(), "%I:%M %p")

    def is_slot_taken(self, date, time_range):
        """Check whether a new event time overlaps an existing event on the same date."""
        try:
            new_start_text, new_end_text = time_range.split(" - ")
            new_start = self.convert_time(new_start_text)
            new_end = self.convert_time(new_end_text)
        except ValueError:
            print("Invalid time format. Use: 9:00 AM - 11:00 AM")
            return True

        for slot in self.event_slots:
            if slot["date"].lower() != date.lower():
                continue

            existing_start_text, existing_end_text = slot["time"].split(" - ")
            existing_start = self.convert_time(existing_start_text)
            existing_end = self.convert_time(existing_end_text)

            overlaps = new_start < existing_end and new_end > existing_start

            if overlaps:
                return True

        return False

    def add_event_slot(self, name, time, date):
        """Add a new event slot if it does not conflict with another."""
        if self.is_slot_taken(date, time):
            return False

        new_slot = {
            "name": name,
            "time": time,
            "date": date
        }

        self.event_slots.append(new_slot)
        save_event_slot(name, time, date)
        return True
    
    def get_event_slots(self):
        """Return all available event slots."""
        return self.event_slots