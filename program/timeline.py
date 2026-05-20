from datetime import datetime
from storage import save_event_slot, load_event_slots


class Timeline:
    def __init__(self):
        self.event_slots = load_event_slots()

    def refresh(self):
        """Reload saved event slots so organizer and student views stay synchronized."""
        self.event_slots = load_event_slots()

    def convert_time(self, time_text):
        """Convert time text like '9:00 AM' into a comparable time value."""
        return datetime.strptime(time_text.strip(), "%I:%M %p")

    def parse_time_range(self, time_range):
        """Convert '9:00 AM - 11:00 AM' into start and end time values."""
        parts = [part.strip() for part in time_range.split("-")]

        if len(parts) != 2:
            raise ValueError("Invalid time format. Use: 9:00 AM - 11:00 AM")

        start_time = self.convert_time(parts[0])
        end_time = self.convert_time(parts[1])

        if end_time <= start_time:
            raise ValueError("Invalid time range. End time must be later than start time.")

        return start_time, end_time

    def validate_slot(self, date, time_range):
        """
        Check whether an event time range is valid and available.

        Returns:
            (True, message) if available
            (False, message) if invalid or conflicting
        """
        try:
            new_start, new_end = self.parse_time_range(time_range)
        except ValueError as error:
            return False, str(error)

        self.refresh()

        for slot in self.event_slots:
            if slot["date"].strip().lower() != date.strip().lower():
                continue

            try:
                existing_start, existing_end = self.parse_time_range(slot["time"])
            except ValueError:
                continue

            overlaps = new_start < existing_end and new_end > existing_start

            if overlaps:
                return (
                    False,
                    "Slot taken. Another event is already scheduled during that date and time."
                )

        return True, "Slot available."

    def is_slot_taken(self, date, time_range):
        """Compatibility helper that returns only True or False."""
        available, _ = self.validate_slot(date, time_range)
        return not available

    def add_event_slot(self, name, time, date):
        """Add a new event slot if it is valid and does not conflict."""
        available, message = self.validate_slot(date, time)

        if not available:
            return False, message

        new_slot = {
            "name": name,
            "time": time,
            "date": date
        }

        self.event_slots.append(new_slot)
        save_event_slot(name, time, date)
        return True, "Event slot saved successfully."

    def get_event_slots(self):
        """Return the latest available event slots."""
        self.refresh()
        return self.event_slots