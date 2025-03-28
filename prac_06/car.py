class Car:
    """Represent a Car object."""

    def __init__(self, name='', fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel or drive until fuel runs out."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
