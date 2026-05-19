class Event:
    def __init__(self, name="Not set", time="Not set", date="Not set"):
        self.name = name
        self.time = time
        self.date = date

    def setDetails(self, name, time, date):
        """Set or update the event details."""
        self.name = name
        self.time = time
        self.date = date

    def viewDetails(self):
        """Return the event details as formatted text."""
        return (
            f"Event Name : {self.name}\n"
            f"Event Time : {self.time}\n"
            f"Event Date : {self.date}"
        )