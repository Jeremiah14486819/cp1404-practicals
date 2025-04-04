class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        # Compare guitars by their year of manufacture
        return self.year < other.year

    def __str__(self):
        return f"{self.name} ({self.year}) - ${self.cost}"

    def __repr__(self):
        return self.__str__()
