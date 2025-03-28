class Guitar:
    def __init__(self, name: str, year: int, cost: float):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self) -> int:
        """Return the age of the guitar based on the current year."""
        from datetime import datetime
        return datetime.now().year - self.year

    def is_vintage(self) -> bool:
        """Determine if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
