class Project:
    def __init__(self, name, priority, completion_percentage):
        self.name = name
        self.priority = priority
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"Project: {self.name}, Priority: {self.priority}, Completion: {self.completion_percentage}%"

    def __repr__(self):
        return self.__str__()
