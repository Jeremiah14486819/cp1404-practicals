class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name} ({self.year}) - Typing: {self.typing}, Reflection: {self.reflection}, Pointer Arithmetic: {self.pointer_arithmetic}"

    def __repr__(self):
        return self.__str__()
